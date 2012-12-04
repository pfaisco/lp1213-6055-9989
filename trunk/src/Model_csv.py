# -*- coding: utf-8 -*-
import csv
"""

"""
class Model_stat(Object):
	"""

	"""
	def __init__(self, file_name, data_list):
		"""

		"""
		self.data = data_list
		self.csvfile = open(file_name, 'wb')

	def write_to_csv(self, file_name , list):
		"""
			escreve os as estatisticas para um csv
		"""
		writer = csv.writer(self.csvfile, delimiter=',')
		for i in list:
			writer.writerow( i )
		
