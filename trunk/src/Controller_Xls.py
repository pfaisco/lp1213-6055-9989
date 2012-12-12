#-*- coding: utf-8 -*-
from Model_Xls import Model_Xls
from xlrd import open_workbook, empty_cell

class Controller_Xls(Model_Xls):
	"""
		Controller Xls Reads info of Major from Xls file
	"""
	def open_Book(self):
		"""
			Opens the book from xls file
		"""
		wb = open_workbook( "./Inscritos_2010-2011 (formato Excel xls).xls", 'rb' )
		s = wb.sheet_by_index( 30 )
		return s	

	def read_xls(self):
		"""
			Read data from cells and return a list with information
		"""
		res_list=[]
		for row_index in range(4, self.sheet.nrows):

			cur = self.sheet.cell_value(row_index,3)
			self.l_major_data.append(cur)
			self.l_major_data += self.get_Major_data(row_index)
			
			if self.check_comp(row_index):
				self.l_years_major = self.get_year_data(row_index)
				self.l_major_data.append(self.l_years_major)
				res_list.append( self.l_major_data)
				
			self.l_major_data=[]
			self.l_years_major=[]
			
		return res_list

	def get_Major_data(self, row_index):
		"""
			Get the a list with information of major name, university, faculty and degree

		"""
		for col_index in range(0,3):
			if self.sheet.cell(row_index,col_index).value != empty_cell.value:
				if col_index==0:
					self.uni=self.sheet.cell_value(row_index,0)
					self.fac=''
					pass
				if col_index==1:
					self.fac=self.sheet.cell_value(row_index,1)
					pass
				if col_index==2:
					self.niv=self.sheet.cell_value(row_index,2)
		l=[self.uni, self.fac, self.niv]
		
		return l

	def check_comp(self, row_index):
		"""
			Check if the Major contains the words "Computadores" and "Informática"
			retrun boolean if exist or not
		"""

		return self.l_major_data[0].find(u'Computadores') > 0 and self.l_major_data[0].find(u'Informática') > 0 	
			
	def get_year_data(self, row_index):
		"""
			Get the number of students per year of each Major
			retrun a list with all years
		"""
		lista_Years=[]	
		for c in (self.Dic_Year.keys()):
			value =self.sheet.cell_value(row_index, c)
			if isinstance(value, float):
				Years=(self.Dic_Year[c], value)
				lista_Years.append(Years)
			else:
				zero = 0.0
				Years=(self.Dic_Year[c], zero)
				lista_Years.append(Years)
		return lista_Years		
