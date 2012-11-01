# -*- coding: utf-8 -*-
from xlrd import open_workbook, cellname, empty_cell
def read_xls():
	wb = open_workbook('Inscritos_2010-2011 (formato Excel xls).xls')
	
	s = wb.sheet_by_index(30)
	
	print 'Sheet:',s.name 
	print empty_cell.value
	
	#file = open( 'tabela.txt' , 'w')
	uni=''
	fac=''
	niv=''
	cur=''

	for row_index in range(4, s.nrows):
		cur = s.cell_value(row_index,3)
		if isinstance(cur, unicode):
			cur = cur.encode('utf8')
		if cur.find('Computadores') > 0 or cur.find('Informática') > 0 :
			for col_index in range(0,2):
				if s.cell(row_index,col_index).value != empty_cell.value:
					if col_index==0:
						uni=s.cell_value(row_index,0)
						pass
					if col_index==1:
						fac=s.cell_value(row_index,1)
						pass
					if col_index==2:
						niv=s.cell_value(row_index,2)
			print uni, fac, niv, cur, '\n'
read_xls()