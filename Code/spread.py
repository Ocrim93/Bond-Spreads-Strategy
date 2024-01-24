import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.api import OLS
from .plotting_lib import plot
from .web_requests import  Yahoo_Web 
from . import utilities
from .Trading_Indicator_Class import Trading_Indicator


class Bond_Spread():



	
	def __init__(self,
				 long_duration_bond : str,
				 short_duration_bond: str,
				 data :  str =  None,
				 start_date : str = None,
				 end_date : str = None,
				 years : int = None):
		
		self.long_duration_bond = long_duration_bond
		self.short_duration_bond = short_duration_bond
		self.data =  self.retrieve_data(start_date,end_date, years)  if data == None else utilities.import_excel_data(data, start_date=start_date, end_date = end_date)
		self.start_date = self.data.index[0] if start_date == None else start_date
		self.end_date = self.data.index[-1] if end_date == None else end_date

		self.avg_spread = float()

	@staticmethod
	def Stationary_Test(data, threshold = 0.05):
		"""
	    Perform Augmented Dickey-Fuller test for stationarity.
	    """
		test = adfuller(data, autolag='AIC')
		print(test)
		p_value = test[1]
		is_stationary = p_value < threshold

		msg = "*** STATIONARY ***" if is_stationary else "not stationary"
		print(f'Series is {msg} (p-value: {p_value:.4f})')
		return p_value


	@staticmethod
	def Compute_Spread(prices : pd.DataFrame(), long_duration_bond :str ,short_duration_bond : str):
		
		label = f'{long_duration_bond} - {short_duration_bond}'

		long_series = prices[long_duration_bond]
		short_series = prices[short_duration_bond]

		# Compute the hedge ratio using Ordinary Least Square (OLS)
		OLS_model  = OLS(long_series,short_series)
		OLS_model = OLS_model.fit()
		hedge_ratio = OLS_model.params[0]

		prices['spread'] = long_series - hedge_ratio*short_series
		
		#Compute Average Spread 
		avg_spread = prices['spread'].mean()

		print(f"Average {label}: {avg_spread:.4f}")
		Bond_Spread.Stationary_Test(prices['spread'])
		return avg_spread,prices
		

	def compute_spread(self):
		self.avg_spread, self.data = Bond_Spread.Compute_Spread(self.data, self.long_duration_bond, self.short_duration_bond)

	def apply_trading_indicator(self, trading_indicator : str , *args):
		indicator = getattr(Trading_Indicator, trading_indicator)
		self.data =  indicator(self.data, *args)
			
	def plotting(self):
		label = f'{long_duration_bond} - {short_duration_bond}'
		plot(self.data, label, 'Date','spread', label, average = self.avg_spread)

	def retrieve_data(self, start_date, end_date, years):
		return Yahoo_Web.get_prices([self.long_duration_bond,self.short_duration_bond],start_date, end_date, years)

			