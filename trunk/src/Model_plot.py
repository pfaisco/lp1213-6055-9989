# -*- coding: utf-8 -*-
import pylab
import matplotlib.ticker
"""
	Module To plot
	include Model and Controller to plot
"""
class Model_Plot():
	"""
		Model Plot has data to create the graph
	"""
	def __init__(self, title, x_list, y_list):
		"""	
			Constructor of class Model Plot stores the x and y data and title
		"""
		self.x_list = x_list
		self.y_list = y_list
		self.title = title

class Controller_Plot(Model_Plot):
	"""
		Class to create graph 
	"""
	def plot_data(self):
		"""
			Plot the data stored on model plot
		"""
		pylab.xticks(range(len(self.x_list)), self.x_list, rotation=30)
		pylab.plot(self.y_list, '-o')
		pylab.title(self.title, fontsize=20)
		pylab.xlabel('Years', fontsize=20)
		pylab.show()