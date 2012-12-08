# -*- coding: utf-8 -*-
import csv
def write_to_csv(file_name , list):
	"""
		escreve os as estatisticas para um csv
	"""
	csvfile = open(file_name, 'wb')
	writer = csv.writer(csvfile, delimiter=',')
	for i in list:
		writer.writerow( i )
	pass
