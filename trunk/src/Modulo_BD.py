# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Float, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref, query

engine = create_engine('sqlite:///./basedado.db', echo = True)
Base = declarative_base(bind = engine)

'''
class Estabelecimento_Ensino(Base):
	__tablename__ = 'Estabelecimento_Ensino'
	nome_Estabelecimento = Column('nome_Estabelecimento', String, primary_key=True)
	Unidade = relationship("Unidade_Organica", backref="Estabelecimento_Ensino")
	
	def __init__(self, nome_Estabelecimento):
		self.nome_Estabelecimento = nome_Estabelecimento

class Unidade_Organica(Base):
	__tablename__='Unidade_Organica'
	nome_Unidade = Column('nome_Unidade', String, primary_key=True)
	nome_Estabelecimento = Column( String, ForeignKey('Estabelecimento_Ensino.nome_Estabelecimento'))
	curso = relationship("Curso", backref="Unidade_Organica")

	def __init__(self, nome_Unidade, nome_Estabelecimento):
		self.nome_Unidade = nome_Unidade
		self.nome_Estabelecimento = nome_Estabelecimento
'''
class Curso(Base):
	'''

	'''
	__tablename__='Curso'
	id = Column(Integer, primary_key = True)
	nome_Curso = Column('nome_Curso', String)
	nome_Unidade = Column('nome_Unidade', String)
	nome_Estabelecimento = Column('nome_Estabelecimento', String)
	nivel_curso = Column( 'nivel_curso', String)
	

	def __init__(self, nome_Curso, nome_Unidade, nivel_curso, nome_Estabelecimento):
		self.nome_Curso = nome_Curso
		self.nome_Unidade = nome_Unidade
		self.nome_Estabelecimento = nome_Estabelecimento
		self.nivel_curso = nivel_curso
	def __repr__(self):
		return self.id
class Ano(Base):
	'''

	'''
	__tablename__='Ano'
	id=Column(Integer, primary_key=True)
	ano = Column('ano', String)
	numero_alunos = Column('numero_alunos', Float)
	curso = relationship("Curso", backref=backref("Ano"))
	id_Curso = Column(Integer, ForeignKey('Curso.id'))
	
	def __init__(self, numero_alunos, ano_c ):
		self.ano = ano_c
		self.numero_alunos = numero_alunos

Base.metadata.create_all()


def insertBD_Curso(nome_Estabelecimento, nome_Unidade, nome_Curso, nivel_curso, l_anos):

	from sqlalchemy.orm import sessionmaker
	Session = sessionmaker(bind = engine)
	s = Session()
	
	c = Curso(nome_Curso = nome_Curso, nome_Unidade = nome_Unidade, nivel_curso = nivel_curso, nome_Estabelecimento= nome_Estabelecimento)
	for a in l_anos:
		c.Ano.extend([Ano(ano_c=a[0], numero_alunos=a[1])])
	s.add(c)
	
	try:
		s.commit()
	except:
		print 'ERROR'


def printBD():
	from sqlalchemy.orm import sessionmaker
	Session = sessionmaker(bind = engine)
	s = Session()

	print s.query(Curso).join(Ano)

	


printBD()
