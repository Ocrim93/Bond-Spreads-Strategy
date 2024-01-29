import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.api import OLS
from .import plotting_lib 
from .web_requests import  Yahoo_Web 
from . import utilities
from .Trading_Indicator_Class import Trading_Indicator


class Bond_Spread():

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
	def Compute_Spread(prices : pd.DataFrame(), long_duration_bond :str ,short_duration_bond : str, hedge_ratio_flag =  True):
		
		label = f'{long_duration_bond} - {short_duration_bond}'

		long_series = prices[long_duration_bond]
		short_series = prices[short_duration_bond]

		if hedge_ratio_flag:
			# Compute the hedge ratio using Ordinary Least Square (OLS)
			OLS_model  = OLS(long_series,short_series)
			OLS_model = OLS_model.fit()
			hedge_ratio = OLS_model.params[0]
		else:
			hedge_ratio = 1 	

		prices['spread'] = long_series - hedge_ratio*short_series

		#Compute Average Spread 
		avg_spread = prices['spread'].mean()
		print(f"Average {label}: {avg_spread:.4f}")
		Bond_Spread.Stationary_Test(prices['spread'])
		return avg_spread,prices
		
	def __init__(self,
				 long_duration_bond : str,
				 short_duration_bond: str,
				 data :  str =  None,
				 start_date : str = None,
				 end_date : str = None,
				 years : int = None):
		
		self.long_duration_bond = long_duration_bond
		self.short_duration_bond = short_duration_bond
		self.data =  self.retrieve_data(start_date,end_date, years)  if data == None else utilities.import_excel_data(data, start_date=start_date, end_date = end_date,years = years)
		self.start_date = self.data.index[0] if start_date == None else start_date
		self.end_date = self.data.index[-1] if end_date == None else end_date
		self.label = f'{self.long_duration_bond} - {self.short_duration_bond}'

		# Derived features
		self.avg_spread = float()
		self.trading_indicators = []
		self.figure = None

	def compute_spread(self):
		self.avg_spread, self.data = Bond_Spread.Compute_Spread(self.data, self.long_duration_bond, self.short_duration_bond)

	def apply_trading_indicator(self, trading_indicator : str , *args):
		indicator = getattr(Trading_Indicator, trading_indicator)
		self.data, field =  indicator(self.data, *args)
		
		# keeping track of the trading indicator
		if isinstance(field,list):
			self.trading_indicators += field
		else:
			self.trading_indicators.append(field)	
			
	def create_figure(self,trading_indicators):
		self.figure = plotting_lib.create_figure(self.data, self.label,'spread')
		self.figure = plotting_lib.adding_horizontal_line(self.figure, self.avg_spread)
		for ind in trading_indicators:
			self.figure = plotting_lib.adding_line(self.figure, self.data, ind)


	def plotting(self, active_trading_indicators = None):
		active_trading_indicators = self.trading_indicators  if active_trading_indicators == None else active_trading_indicators

		self.create_figure(active_trading_indicators)
		plotting_lib.plot(self.figure)

	def plotting_yield(self):
		self.figure = plotting_lib.create_figure(self.data,self.label,self.long_duration_bond)
		self.figure = plotting_lib.adding_line(self.figure, self.data, self.short_duration_bond)
		plotting_lib.plot(self.figure)

	def retrieve_data(self, start_date, end_date, years):
		return Yahoo_Web.get_prices([self.long_duration_bond,self.short_duration_bond],start_date, end_date, years)


class Bond_Spread_return(Bond_Spread):
	
	@staticmethod
	def compute_return(data):
		
		fields = list(data.columns)
		return_df = data.copy()

		for bond in fields:
			return_df[bond] = data[bond].pct_change()
			return_df[bond][0] = 0
			print(return_df)
		
		return return_df

	def __init__(self,
				 long_duration_bond : str,
				 short_duration_bond: str,
				 data :  str =  None,
				 start_date : str = None,
				 end_date : str = None,
				 years : int = None):

		super().__init__( long_duration_bond,
				 		  short_duration_bond,
				 		  data,
				          start_date,
				          end_date,
				          years)

		self.data = Bond_Spread_return.compute_return(self.data)
		self.label = self.label + '_return'



	# Override of compute_spread method
	def compute_spread(self):
		self.avg_spread, self.data = Bond_Spread.Compute_Spread(self.data, self.long_duration_bond, self.short_duration_bond,hedge_ratio_flag = False)
		























			