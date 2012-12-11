# -*- coding: utf-8 -*-
import csv
"""
	Dealls with csv creation
"""
class Model_stat(object):
	"""
		Stores information to make csv files
	"""
	def __init__(self, file_name):
		"""
			Constructor of class Model_stat
		"""
		self.file_name = file_name
		self.csvfile = open(self.file_name, 'wb')
		print 'opening file....'

class Controller_stat(Model_stat):
	"""
		Class controller of csv 
	"""
	
	def write_to_csv(self, l):
		"""
			wirte statistics to Csv File
		"""
		
		writer = csv.writer(self.csvfile, delimiter=',')
		
		for i in l:
			writer.writerow( i )
			print i

		self.csvfile.close()