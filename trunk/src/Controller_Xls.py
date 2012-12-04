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

ctl_xls = Controller_Xls()
ctl_xls.read_xls()			



# def read_xls():
# 	"""
	

# 	"""

# 	wb = open_workbook('Inscritos_2010-2011 (formato Excel xls).xls')
# 	s = wb.sheet_by_index(30)
# 	uni=''
# 	fac=''
# 	niv=''
# 	cur=''

# 	lista_anos=[]
# 	dic={7:'1995/96', 10:'1996/97', 13:'1997/98', 16:'1998/99', 19:'1999/00' ,22:'2000/01', 25:'2001/02', 28:'2002/03', 31:'2003/04', 34:'2004/05', 37:'2005/06', 40:'2006/07', 43:'2007/08', 47:'2008/09', 50:'2009/10', 53:'2010/11'}
	
# 	for row_index in range(4, s.nrows):
# 		cur = s.cell_value(row_index,3).encode('utf-8')
		
		
		
# 		for col_index in range(0,3):
# 			if s.cell(row_index,col_index).value != empty_cell.value:
# 				if col_index==0:
# 					uni=s.cell_value(row_index,0).encode('utf-8')
# 					fac=''
# 					pass
# 				if col_index==1:
# 					fac=s.cell_value(row_index,1).encode('utf-8')
# 					pass
# 				if col_index==2:
# 					niv=s.cell_value(row_index,2).encode('utf-8')
		
# 		if cur.find('Computadores') > 0 and cur.find('Informática') > 0 :	
# 			for c in (LIST_COL_YEARS):
# 				#print dic[c] + ' - ' + str(s.cell_value(row_index, c))
# 				value =s.cell_value(row_index, c)
# 				#valores nao numericos nao sao adicionados a db
# 				if isinstance(value, float):
# 					anos=(dic[c], value)
# 					lista_anos.append(anos)
# 				else:
# 					z = 0.0
# 					anos=(dic[c], z)
# 					lista_anos.append(anos)
			
# 			bd.insertBD_Curso(name_Estabelecimento=unicode(uni, 'utf8'), name_Unidade=unicode(fac,'utf8'), name_Curso=unicode(cur,'utf8'), nivel_curso=unicode(niv, 'utf8'), l_anos= lista_anos)	
# 			lista_anos=[]
