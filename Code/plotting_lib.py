from plotly.graph_objs import Figure, Scatter
from plotly.offline import  iplot
from Constant import PATH_folder, GRAPH
import plotly.io as pio 
import random
from typing import Union

import plotly.express as px

colors = ['#1F77B4']
def generator_colour():
	global colors
	
	color =  '#' + ''.join([random.choice('ABCDEF0123456789') for i in range(6)]) 
	if color in colors:
		generator_colour()
	else:
		colors.append(color)	
		return color 

def setting_layout(figure,title):

	figure.update_layout(
		    font_family= GRAPH.font_family.value,
		    font_color=GRAPH.font_color.value,
		    title_font_family=GRAPH.title_font_family.value,
		    title_font_color=GRAPH.title_font_color.value,
		    legend_title_font_color=GRAPH.legend_title_font_color.value,
		    title=dict(text=title , font=dict(size=GRAPH.title_font_size.value),automargin=True, yref='paper')
    )

	return figure

def create_figure(	data, 
				    title,
					y_axis_name ):
	
	figure = Figure(Scatter(x=data.index, y=data[y_axis_name],mode='lines', name = y_axis_name, line = {'color' : generator_colour()}))
	figure = setting_layout(figure,title)
	
	return figure	

def adding_horizontal_line(figure, value, name = 'avg'):
	color = generator_colour() 
	figure.add_hline(y=value, annotation_text='{:.4f}'.format(value), 
		              annotation_position="bottom right",
		              annotation_font_size=13,
		              annotation_font_color=color ,line= {'color' :color })
	return figure

def adding_line(figure, data, field ):
	color = generator_colour()
	# check we need to add two lines same colour
	if not isinstance(field,tuple):
		field = [field]
	for y_name in  field:
		figure.add_trace(Scatter(x=data.index, y=data[y_name], mode='lines', name = y_name, line = {'color' : color}))
	return figure	


def plot(figure, file_name = None, extension = 'png' ):
	if file_name == None:
		file_name = figure.layout['title']['text']
	iplot(figure)
	pio.write_image(figure,f'{PATH_folder.Image.value}{file_name}.{extension}', format = extension)

