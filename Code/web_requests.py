import yfinance as yf
import datetime as dt
from typing import Union 


class Yahoo_Web():
	def __init__(self):
		pass

	@staticmethod
	def get_prices(tickers : Union[str,list], 
					start_date :  dt.datetime = None,  
					end_date : dt.datetime = None , 
					years = int | None):
	
		end_date =  dt.datetime.now() if end_date == None else end_date
		if years != None:
			start_date = end_date - dt.timedelta(days = years*365)
		data = 	yf.download(tickers, start= start_date, end = end_date)
		data.sort_index(  inplace =True)
		data['Adj Close'].to_csv(f'./Input/{tickers[1]}-{tickers[0]}_{end_date}-{start_date}.csv')
		return data['Adj Close']

