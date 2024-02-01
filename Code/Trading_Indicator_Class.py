import pandas as pd

class Trading_Indicator():

	def __init__(self):
		pass 
	
	@staticmethod
	def EMA(price_data : pd.DataFrame(), window,adjust=False, column = 'spread'):
		'''
			Exponential Moving Average
		'''
		field = f'EMA_{window}'
		price_data[field] = price_data[column].ewm(span=window, adjust=False).mean()
		return price_data, field
	
	@staticmethod
	def SMA(price_data : pd.DataFrame(), window, column = 'spread'):
		'''
			Simple Moving Average
		'''
		field = f'SMA_{window}'
		price_data[field] = price_data[column].rolling(window=window).mean()
		return price_data, field 

	@staticmethod
	def STD(price_data : pd.DataFrame(), window, column = 'spread'):
		'''
			Simple Moving Average
		'''
		field = f'STD_{window}'
		price_data[field] = price_data[column].rolling(window=window).std(ddof =1 )
		price_data[field]=price_data[field].bfill()
		return price_data, field

	@staticmethod
	def Z_score(price_data : pd.DataFrame(), mean_column , std_column  ,column = 'spread' ):
		'''
			Z_score and Z_score bands
		'''
		field = ['Z_score']
		num_std =[1,2]
		price_data['Z_score'] = (price_data[column] - price_data[mean_column])/(price_data[std_column])

		for i in num_std:
			price_data[f'Z_UPPER{i}'] = +i
			price_data[f'Z_LOWER{i}'] = -i
			field.append((f'Z_UPPER{i}', f'Z_LOWER{i}'))
		return price_data, field



	@staticmethod
	def Bollinger_Bands(price_data : pd.DataFrame(), mean_column , std_column ,num_std : list  = [1], column = 'spread', ):
		'''  Bollinger Bands
    		Compute Bollinger Bands as a multiple of number of standard deviations specified by num_std hyper-parameter	
    	'''	
		field = []
		print(f'Bollinger_Bands {mean_column} - {std_column}')
		for i in num_std:
			price_data[f'BB_UPPER{i}'] = price_data[mean_column] +  i*price_data[std_column] 
			price_data[f'BB_LOWER{i}'] = price_data[mean_column] -  i*price_data[std_column] 
			field.append((f'BB_UPPER{i}', f'BB_LOWER{i}'))

		return price_data, field
