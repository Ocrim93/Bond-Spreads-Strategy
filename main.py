# US Treasury Spread Tickers and Chart Labels
from Code.web_requests import  Yahoo_Web
from Code.spread import Bond_Spread,Bond_Spread_return
from Code import utilities

utilities.create_folder()

'''
import yfinance as yf
import pprint,pandas as pd
import datetime
#data = 	yf.download(tickers, start= start_date, end = end_date)
ticker = yf.Ticker("PRX.AS")

startDate = datetime.datetime(2019, 5, 31)
 
# endDate , as per our convenience we can modify
endDate = datetime.datetime(2021, 1, 30)
history =  ticker.history(start=startDate, end=endDate)

pprint.pprint(ticker.history_metadata)

d 
# whole python dictionary is printed here
pprint.pprint(ticker.info)
for key,value in ticker.info.items():
	if 'float' in key:
		print(key,value)
pd.set_option('display.max_rows', None)
print(GetFacebookInformation.info.history(start=startDate, end=endDate))


'''


#label1 = '5Y - 2Y'
bond_tickers = ['^IRX', '^FVX']

spread = Bond_Spread(data = './Input/data.csv',
				 long_duration_bond  = bond_tickers[0],
				 short_duration_bond= bond_tickers[1],
				 years = 3)
spread.plotting_yield()
spread.compute_spread()
spread.apply_trading_indicator('EMA' ,14)
spread.apply_trading_indicator('EMA' ,50)
spread.apply_trading_indicator('EMA' ,200)
spread.apply_trading_indicator('STD' ,20)

spread.apply_trading_indicator('Bollinger_Bands' )
#	def Bollinger_Bands(price_data : pd.DataFrame(), num_std : list[int] = [1], column = 'spread', mean_column = 'EMA', std_column = 'STD'):

spread.plotting()
print(spread.data)






# US Treasury Spread Tickers and Chart Labels
#label1 = '5Y - 2Y'
#bond_tickers1 = {'^IRX', '^FVX'}
#label2 = '10Y - 2Y'
#bond_tickers2 = {'^TNX', '^IRX'}
#label3 = '10Y - 5Y'
#bond_tickers3 = {'^TNX', '^FVX'}
    