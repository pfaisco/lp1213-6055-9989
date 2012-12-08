# -*- coding: utf-8 -*-
import csv
"""

"""
class Model_stat(object):
	"""

	"""
	def __init__(self, file_name):
		"""

		"""
		self.file_name = file_name
		self.csvfile = open(self.file_name, 'wb')
		print 'opening file....'

class Controller_stat(Model_stat):
	"""

	"""
	
	def write_to_csv(self, l):
		"""
			escreve os as estatisticas para um csv
		"""
		print 'writing....'
		writer = csv.writer(self.csvfile, delimiter=',')
		print 'writing....'
		for i in l:
			writer.writerow( i )
			print 'writing....'

		self.csvfile.close()