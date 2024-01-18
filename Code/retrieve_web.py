import yfinance as yf
import datetime as dt
from typing import Union 


class Yahoo_Web():
	def __init__(self):
		pass

	@staticmethod
	def get_prices(tickers : Union[str,list], 
					start_date :  dt.datetime = None,  
					end_date : dt.datetime = dt.datetime.now() , 
					years = int | None  ):
		if years != None:
			start_date = end_date - dt.timedelta(days = years*365)
		data = 	yf.download(tickers, start= start_date, end = end_date)
		return data

