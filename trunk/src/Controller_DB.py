# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Float, String, Integer, distinct, func
from sqlalchemy.orm import query, sessionmaker
from Model_DB import Curso, Ano, modelDB
import os

class Controller_DB(modelDB):
	
	def create_db(self):
		os.system('python Model_DB.py')


	def insertBD_Curso(self, name_Estabelecimento, name_Unidade, name_Curso, nivel_curso, l_anos):
		"""

		"""
		s = self.create_session()
		c = Curso(name_Curso = name_Curso, name_Unidade = name_Unidade, nivel_curso = nivel_curso, name_Estabelecimento= name_Estabelecimento)
		for a in l_anos:
			c.Ano.extend([Ano(ano_c=a[0], numero_alunos=a[1])])
		s.add(c)
		s.commit()
		try:
			s.commit()
		except:
			print 'ERROR_Commit'

	def create_session(self):
		"""

		"""
		Session = sessionmaker(bind = self.engine)
		s = Session()
		return s

	##################################################################
	#
	#		QUERY
	#
	##################################################################
	def query_cursos_info(self):
		"""
			Metodo Query Lista de Cursos
		"""
		s = self.create_session()
		l = s.query(Curso).all()
		return l
	
	def query_major(self):
		"""

		"""
		s = self.create_session()
		l = s.query(Curso.name_Curso, Curso.name_Estabelecimento, Curso.nivel_Curso).all()
		res = []
		for i in l:
			s = i[0] + ' | ' + i[1] + ' | ' + i[2]
			res.append(s)

		return res

	def query_degree(self):
		"""

		"""
		s = self.create_session()
		l = s.query(distinct(Curso.nivel_Curso)).all()
		res = []
		for i in l:
			res.append(i[0])
		return res

	def query_curso_funcionamento(self):
		"""
			Anos em que os cursos estiveram em funcionamento
		"""
		s = self.create_session()
		q_c = self.query_cursos_info()
		res=[]
		for c in q_c:
			curso_info=[]
			curso_info.append(c.name_Curso.encode('utf-8'))
			curso_info.append(c.name_Estabelecimento.encode('utf-8'))
			curso_info.append(c.name_Unidade.encode('utf-8'))
			curso_info.append(c.nivel_Curso.encode('utf-8'))

			x = s.query(Ano).filter(Ano.id_Curso == c.id).all()
		
			for a in x:
				if a.numero_alunos > 0:   
					curso_info.append(a.ano)
			res.append(curso_info)
		return res

	def query_alunos_niveis(self, level = None):
		"""
			Contagem de alunos por nivel ano
		"""
		s = self.create_session()
	
		cont = s.query(Curso.nivel_Curso, Ano.ano, func.sum(Ano.numero_alunos)).join(Ano).filter(Curso.id == Ano.id_Curso).group_by(Curso.nivel_Curso, Ano.ano).all()
		res=[]
		for i in cont:
			res.append((i[0].encode('utf-8'),i[1], i[2]))
		return res
		

	def query_alunos_curso(self):
		"""
			Contagem de alunos por curso ano
		"""
		s = self.create_session()
		cont = s.query(Curso.name_Curso, Ano.ano, func.sum(Ano.numero_alunos)).join(Ano).filter(Curso.id == Ano.id_Curso).group_by(Curso.id, Ano.ano).all()
		res=[]
		for i in cont:
			res.append((i[0].encode('utf-8'),i[1], i[2]))
		return res	
		
	def query_curso_nivel(self):
		"""
			Contagem de cursos por nivel ano
			select Curso.nivel_curso , ano.ano, count( curso.id )
				from Curso  join ano where curso.id == id_curso 
				group by  ano.ano, curso.name_curso;
		"""
		s = self.create_session()
		cont = s.query(Curso.nivel_Curso, Ano.ano, func.count(Curso.id)).join(Ano).filter(Curso.id == Ano.id_Curso).group_by(Ano.ano, Curso.name_Curso).all()
		res=[]
		for i in cont:
			res.append((i[0].encode('utf-8'),i[1], i[2]))
		return res	
	def query_alunos_curso_plot(self, id_Curso):
		"""
			Contagem de alunos por curso ano  
		"""
		s = self.create_session()
		cont = s.query(Curso.name_Curso, Ano.ano, func.sum(Ano.numero_alunos)).join(Ano).filter(Curso.id == id_Curso).group_by(Curso.id, Ano.ano).all()
		res=[]
		for i in cont:
			res.append((i[0].encode('utf-8'),i[1], i[2]))
		return res	
	