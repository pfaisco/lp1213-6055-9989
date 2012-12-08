# -*- coding: utf-8 -*-
'''
	Modulo main
	Corre o programa sequencialmente para fins de teste durante o desenvolvimento


	@author: Pedro Faísco


'''
import Modulo_Xls_v1 as xls
import Modulo_BD as bd
import Modulo_stat as stat

if __name__ == '__main__':
	#bd.qnt_alunos(True)
	#bd.nivel()
	#l = bd.query_Curso()
	#stat.write_to_csv(file_name = 'meuprimeirocsv.csv', list = l)
	# x = bd.query_contagem_niveis()
	# stat.write_to_csv(file_name = 'meusegundocsv.csv', list = x)
	# x = bd.query_contagem_Curso_alunos()
	# stat.write_to_csv(file_name = 'meu3csv.csv', list = x)
	x = bd.query_contagem_nivel_curso()
	stat.write_to_csv(file_name = 'meu4csv.csv', list = x)