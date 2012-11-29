# -*- coding: utf-8 -*-
from xlrd import open_workbook, cellname, empty_cell
#import Modulo_BD as bd
import Modulo_BD as bd

COL_ANO_95_96 = 7
COL_ANO_96_97 = 10
COL_ANO_97_98 = 13
COL_ANO_98_99 = 16
COL_ANO_99_00 = 19
COL_ANO_00_01 = 22
COL_ANO_01_02 = 25
COL_ANO_02_03 = 28
COL_ANO_03_04 = 31
COL_ANO_04_05 = 34
COL_ANO_05_06 = 37
COL_ANO_06_07 = 40
COL_ANO_07_08 = 43
COL_ANO_08_09 = 47
COL_ANO_09_10 = 50
COL_ANO_10_11 = 53

LIST_COL_ANOS = [COL_ANO_95_96,
				COL_ANO_96_97,
				COL_ANO_97_98,
				COL_ANO_98_99,
				COL_ANO_99_00,
				COL_ANO_00_01,
				COL_ANO_01_02,
				COL_ANO_02_03,
				COL_ANO_03_04,
				COL_ANO_04_05,
				COL_ANO_05_06,
				COL_ANO_06_07,
				COL_ANO_07_08,
				COL_ANO_08_09,
				COL_ANO_09_10,
				COL_ANO_10_11]


def read_xls():
	'''
	

	'''

	wb = open_workbook('Inscritos_2010-2011 (formato Excel xls).xls')
	s = wb.sheet_by_index(30)
	uni=''
	fac=''
	niv=''
	cur=''
	count=0
	lista_anos=[]
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
		if cur.find('Computadores') > 0 and cur.find('Informática') > 0 :	
			for c in (LIST_COL_ANOS):
				#print dic[c] + ' - ' + str(s.cell_value(row_index, c))
				value =s.cell_value(row_index, c)
				#valores nao numericos nao sao adicionados a db
				if isinstance(value, float):
					anos=(dic[c], value)
					lista_anos.append(anos)
				else:
					z = 0.0
					anos=(dic[c], z)
					lista_anos.append(anos)
			bd.insertBD_Curso(nome_Estabelecimento=unicode(uni, 'utf8'), nome_Unidade=unicode(fac,'utf8'), nome_Curso=unicode(cur,'utf8'), nivel_curso=unicode(niv, 'utf8'), l_anos= lista_anos)	
			lista_anos=[]


if __name__ == '__main__':
	read_xls()


