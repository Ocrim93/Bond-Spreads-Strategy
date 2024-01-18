import datetime 
import logging 
import os
from Constant import PATH_file
import sys 
import time 


def calculate_time(func):
	
	def inner_func(*args, **kwargs):
		start_time = datetime.datetime.now()

		return_value = func(*args, **kwargs)

		end_time = datetime.datetime.now()
		print('Total time taken in {}  {:><10}'.format(func.__name__, str(end_time - start_time)))

		return return_value


	return inner_func

def write_log(msg : str | None ):
	if (not os.path.exists(PATH_file.Logging.value)):
		logging.basicConfig(filename = PATH_file.Logging.value, filemode= 'w', level = logging.INFO)
		logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

	logging.info('%s%s%s', time.strftime('%d/%m/%Y %H:%M:%S'), '  @@@@  -->  ', msg  )
