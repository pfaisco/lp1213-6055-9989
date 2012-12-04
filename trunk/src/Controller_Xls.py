#-*- coding: utf-8 -*-
from Model_Xls import Model_Xls
from xlrd import open_workbook, empty_cell

class Controller_Xls():
	uni, fac, niv = '', '', ''
	def __init__(self):
		self.sheet = self.open_Book()
		self.l_major_data = []
		self.l_years_major = []
		model = Model_Xls()
		self.dic = model.get_dic()
	
	def open_Book(self, name = "./Inscritos_2010-2011 (formato Excel xls).xls", sheet = 30 ):
		"""

		"""
		wb = open_workbook( name, 'rb' )
		s = wb.sheet_by_index(sheet)
		return s	

	def read_xls(self):
		"""

		"""
		for row_index in range(4, self.sheet.nrows):
			cur = self.sheet.cell_value(row_index,3).encode('utf-8')
			self.l_major_data = self.get_Major_data(row_index)
			self.l_major_data.append(cur)
			if self.check_comp(row_index):
				self.l_years_major = self.get_year_data(row_index)
				self.l_major_data.append(self.l_years_major)
				print self.l_major_data
			
			self.l_major_data=[]
			self.l_years_major=[]

	def get_Major_data(self, row_index):
		"""

		"""
		global uni, fac, niv 
		for col_index in range(0,3):
			if self.sheet.cell(row_index,col_index).value != empty_cell.value:
				if col_index==0:
					uni=self.sheet.cell_value(row_index,0).encode('utf-8')
					fac=''
					pass
				if col_index==1:
					fac=self.sheet.cell_value(row_index,1).encode('utf-8')
					pass
				if col_index==2:
					niv=self.sheet.cell_value(row_index,2).encode('utf-8')
		return [uni, fac, niv]

	def check_comp(self, row_index):
		"""

		"""
		return self.l_major_data[3].find('Computadores') > 0 and self.l_major_data[3].find('Informática') > 0 	
			
	def get_year_data(self, row_index):
		"""

		"""
		lista_anos=[]	
		for c in (self.dic.keys()):
			value =self.sheet.cell_value(row_index, c)
			if isinstance(value, float):
				anos=(self.dic[c], value)
				lista_anos.append(anos)
			else:
				zero = 0.0
				anos=(self.dic[c], zero)
				lista_anos.append(anos)
		return lista_anos		

