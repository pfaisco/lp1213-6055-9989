# -*- coding: utf-8 -*-
from xlrd import open_workbook, cellname, empty_cell
#import Modulo_BD as bd
import Modulo_BD as bd
def read_xls():
	wb = open_workbook('Inscritos_2010-2011 (formato Excel xls).xls')
	s = wb.sheet_by_index(30)
	uni=''
	fac=''
	niv=''
	cur=''
	count=0
	dic={7:'1995/96', 10:'1996/97', 13:'1997/98', 16:'1998/99', 19:'1999/00' ,22:'2000/01', 25:'2001/02', 28:'2002/03', 31:'2003/04', 34:'2004/05', 37:'2005/06', 40:'2006/07', 43:'2007/08', 47:'2008/09', 50:'2009/10', 53:'2010/11'}
	for row_index in range(4, s.nrows):
		cur = s.cell_value(row_index,3)
		if isinstance(cur, unicode):
			cur = cur.encode('utf-8')
		for col_index in range(0,3):
			if s.cell(row_index,col_index).value != empty_cell.value:
				if col_index==0:
					uni=s.cell_value(row_index,0).encode('utf-8')
					fac=''
					pass
				if col_index==1:
					fac=s.cell_value(row_index,1).encode('utf-8')
					pass
				if col_index==2:
					niv=s.cell_value(row_index,2).encode('utf-8')
		if cur.find('Computadores') > 0 or cur.find('Informática') > 0 :	
			#print (cur)
			#count+=1
			bd.insertBD_Curso(nome_Estabelecimento=unicode(uni, 'utf8'), nome_Unidade=unicode(fac,'utf8'), nome_Curso=unicode(cur,'utf8'), nivel_curso=unicode(niv, 'utf8'))
			for c in (7, 10, 13, 16, 19 ,22, 25, 28, 31, 34, 37, 40, 43, 47, 50, 53):
				#print dic[c] + ' - ' + str(s.cell_value(row_index, c))
				value =s.cell_value(row_index, c)
				if isinstance(value, float):
					bd.insert_Ano(nome_Curso=unicode(cur, 'utf8'), ano=dic[c], numero_alunos=value)
read_xls()


