import os
from Code.debugging_method import write_log
from Constant import PATH_folder

def create_folder():
	# ---------- Create folder -----------
	for folder in  list(PATH_folder):
		if not os.path.exists(folder.value):
			os.mkdir(folder.value)
			write_log('Create folder {}'.format(folder.value))


# Method to read bond data from an Excel file
def import_excel_data(file_path, start_date = None , end_date = None):
	
	if ':' in file_path:
		file_path,sheet_name = file_path.split(':')
	else:
		sheet_name = 0
	# import data
   
	df = pd.read_excel(file_path, sheet_name=sheet_name)
	df.sort_values(by='Date', ignore_index= True,inplace=True)
    
	start_date = df.loc[0,'Date']if start_date == None else start_date
	end_date = df.loc[df.shape[0]-1 ,'Date'] if end_date == None else end_date 
    
	# filter data to match our choosen date range
	filtered_df = df[(df['Date'] >= start_date) & (df[DATE] <= end_date)]
	
	# set date column as index
	filtered_df.set_index('Date', inplace=True)
    
	return filtered_df