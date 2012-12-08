# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Float, String, Integer, distinct, func
from sqlalchemy.orm import query, sessionmaker
from Modulo_BD import Curso, Ano, modelDB

class Controller_DB():

	def __init__(self, name = './basedados.db'):
		'''

		'''
		# db_file = open(name, 'w')
		# db_file.close()
		self.nameBD = 'sqlite:///' + name
		print self.nameBD
		self.engine = create_engine(self.nameBD, echo = True)
		#self.Base = declarative_base(bind = self.engine)
		

	def insertBD_Curso(self, name_Estabelecimento, name_Unidade, name_Curso, nivel_curso, l_anos):
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
		Session = sessionmaker(bind = self.engine)
		s = Session()
		return s


	##################################################################
	#
	#		QUERY
	#
	##################################################################
	def query_name_cursos(self):
		"""
			Metodo Query Lista de Cursos
		"""
		s = self.create_session()
		l = s.query(Curso).all()
		return l

	def query_nivel(self):
		s = self.create_session()
		l = s.query().query(Curso.nivel_Curso).all()
		pass


	def query_curso_funcionamento(self):
		"""
			Anos em que os cursos estiveram em funcionamento
		"""
		s = self.create_session()
		q_c = query_name_cursos()
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

	def query_alunos_niveis(self):
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
		s = self.self.create_session()
		cont = s.query(Curso.nivel_Curso, Ano.ano, func.count(Curso.id)).join(Ano).filter(Curso.id == Ano.id_Curso).group_by(Ano.ano, Curso.name_Curso).all()
		res=[]
		for i in cont:
			res.append((i[0].encode('utf-8'),i[1], i[2]))
		return res	

if __name__ == '__main__':
	ctr = Controller_DB()

	

	l_anos=[('99',2),('23',324),('234',234)]
	ctr.insertBD_Curso(name_Estabelecimento=unicode('uni', 'utf8'), 
		name_Unidade = unicode('fac','utf8'), 
		name_Curso = unicode('cur','utf8'), 
		nivel_curso = unicode('niv', 'utf8'), 
		l_anos = l_anos)