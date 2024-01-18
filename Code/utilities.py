import os
from Code.debugging_method import write_log
from Constant import PATH_folder

def create_folder():
	# ---------- Create folder -----------
	for folder in  list(PATH_folder):
		if not os.path.exists(folder.value):
			os.mkdir(folder.value)
			write_log('Create folder {}'.format(folder.value))
