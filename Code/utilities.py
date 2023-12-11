import logging 
import os
from Constant import PATH
import sys 
import time 


def write_log(msg : str | None ):
	file_log = PATH.Outcome.value + PATH.File_Logging.value
	if (not os.path.exists(PATH.Outcome.value + PATH.File_Logging.value)):
		logging.basicConfig(filename = file_log, filemode= 'w', level = logging.INFO)
		logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

	logging.info('%s%s%s', time.strftime('%d/%m/%Y %H:%M:%S'), ' @@ -->  ', msg  )
