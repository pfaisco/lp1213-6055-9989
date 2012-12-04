# -*- coding: utf-8 -*-
import pylab

import Modulo_BD as bd
import matplotlib.ticker


lista = bd.query_alunos_niveis()
x=[]
y=[]

for i in lista:
	
	if i[0].find('L1 - Licenciatura') >= 0:
		x.append(i[1])
		y.append(i[2])
		


pylab.xticks(range(len(x)), x, rotation=30)
pylab.plot(y, '-o')
pylab.title('Grafico Alunos por ano no nivel Academico', fontsize=20)
# shorthand is also supported and curly's are optional
pylab.xlabel('Anos', fontsize=20)

pylab.show()

