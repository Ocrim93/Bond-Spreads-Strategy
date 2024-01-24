import pandas as pd

class Trading_Indicator():

	def __init__(self):
		pass 

	@staticmethod
	def EMA(price_data : pd.DataFrame(), window,adjust=False, column = 'spread'):
		'''
			Exponential Moving Average
		'''
		price_data[f'EMA_{window}'] = price_data[column].ewm(span=window, adjust=False).mean()
		return price_data
	
	@staticmethod
	def SMA(price_data : pd.DataFrame(), window, column = 'spread')
		'''
			Simple Moving Average
		'''
		price_data[f'SMA_{window}'] = price_data[column].rolling(window=window).mean()
		return price_data

		