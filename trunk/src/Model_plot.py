# -*- coding: utf-8 -*-
import pylab
import matplotlib.ticker
"""

"""
class Model_Plot(Object):
	"""

	"""
	def __init__(self, title, x_list, y_list):
		"""

		"""
		self.x_list = x_list
		self.y_list = y_list
		self.title = title

	def plot_data(self):
		"""

		"""
		pylab.xticks(range(len(self.x_list)), self.x_list, rotation=30)
		pylab.plot(self.y_list, '-o')
		pylab.title(self.title, fontsize=20)
		pylab.xlabel('Anos', fontsize=20)
		pylab.show()

