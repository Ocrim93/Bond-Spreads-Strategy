from plotly.graph_objs import Figure, Scatter
from plotly.offline import  iplot
from Constant import PATH_folder, GRAPH
import plotly.io as pio 


import plotly.express as px


def setting_layout(figure):

	figure.update_layout(
		    font_family= GRAPH.font_family.value,
		    font_color=GRAPH.font_color.value,
		    title_font_family=GRAPH.title_font_family.value,
		    title_font_color=GRAPH.title_font_color.value,
		    legend_title_font_color=GRAPH.legend_title_font_color.value
    )
	return figure

def plot(data, 
		title, 
		x_axis_name , 
		y_axis_name ,
		file_name = None ,
		extension = 'png',
		average = None):
	
	if file_name == None:
		file_name = title 
	#figure = Figure(Scatter(x=data.index, y=data[y_axis_name], yaxis = 'f',  mode='lines', name= name))
	figure = px.line(data, x =data.index, y = y_axis_name, title = title )
	figure = setting_layout(figure)
	
	if average != None:
		figure.add_hline(y=average, line= {'color' : 'red' })
	iplot(figure)
	pio.write_image(figure,f'{PATH_folder.Image.value}{file_name}.{extension}', format = extension)

