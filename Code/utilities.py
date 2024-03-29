import os
from Code.debugging_method import write_log
from Constant import PATH_folder
import pandas as pd
import datetime as dt


def create_folder():
	# ---------- Create folder -----------
	for folder in  list(PATH_folder):
		if not os.path.exists(folder.value):
			os.mkdir(folder.value)
			write_log('Create folder {}'.format(folder.value))


# Method to read bond data from an Excel file
def import_excel_data(file_path, start_date = None , end_date = None, years : int = None):
	
	if ':' in file_path:
		file_path,sheet_name = file_path.split(':')
	else:
		sheet_name = 0
	# import data
	if '.csv' in file_path:
  		df = pd.read_csv(file_path)
	else:	
		df = pd.read_excel(file_path, sheet_name=sheet_name)
	df['Date'] = pd.to_datetime(df['Date'])	
	df.sort_values(by='Date', ignore_index= True,inplace=True)
	end_date = df.loc[df.shape[0]-1 ,'Date'] if end_date == None else end_date 

	if years != None :
		start_date = end_date- dt.timedelta(days = years*365)
	else:
		
		start_date = df.loc[0,'Date'] if start_date == None else start_date
	# filter data to match our choosen date range
	filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
	
	# set date column as index
	filtered_df.set_index('Date', inplace=True)
    
	return filtered_df

	