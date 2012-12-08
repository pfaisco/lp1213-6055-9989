# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Float, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref

class modelDB(object):
	"""

	"""
	
	def __init__(self, name = 'sqlite:///./basedados.db'):
		"""

		"""
		self.engine = create_engine(name, echo = True)
		self.Base = declarative_base(bind = self.engine)
		
		
m = modelDB()
Base = m.Base

class Curso(Base):
	"""

	"""
	__tablename__='Curso'
	id = Column(Integer, primary_key = True)
	name_Curso = Column('name_Curso', String)
	name_Unidade = Column('name_Unidade', String)
	name_Estabelecimento = Column('name_Estabelecimento', String)
	nivel_Curso = Column( 'nivel_Curso', String)
	
	def __init__(self, name_Curso, name_Unidade, nivel_curso, name_Estabelecimento):
		"""

		"""
		self.name_Curso = name_Curso
		self.name_Unidade = name_Unidade
		self.name_Estabelecimento = name_Estabelecimento
		self.nivel_Curso = nivel_curso
	
class Ano(Base):
	"""

	"""
	__tablename__='Ano'
	id=Column(Integer, primary_key=True)
	ano = Column('ano', String)
	numero_alunos = Column('numero_alunos', Float)
	curso = relationship("Curso", backref=backref("Ano"))
	id_Curso = Column(Integer, ForeignKey('Curso.id'))
	
	def __init__(self, numero_alunos, ano_c ):
		"""

		"""
		self.ano = ano_c
		self.numero_alunos = numero_alunos

if __name__ == '__main__':
	m.Base.metadata.create_all()