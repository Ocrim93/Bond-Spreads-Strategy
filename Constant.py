from enum import Enum


class PATH_folder(Enum):
	Outcome = './Outcome/'
	Code = './Code/'
	Image = Outcome +'Images/'

class PATH_file(Enum):
	Logging = PATH_folder.Outcome.value + 'BondStrategy.log'

class GRAPH(Enum):
	font_family="Courier New"
	font_color="blue"
	title_font_family="Times New Roman"
	title_font_color="blue"
	title_font_size = 20
	legend_title_font_color="green"
