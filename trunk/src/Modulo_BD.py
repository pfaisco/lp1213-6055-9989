# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Float, String, ForeignKey

engine = create_engine('sqlite:///./basedado.db', echo=True)
Base = declarative_base(bind=engine)


class Estabelecimento_Ensino(Base):
	__tablename__ = 'Estabelecimento_Ensino'
	nome_Estabelecimento = Column('nome_Estabelecimento', String, primary_key = True)
	
	def __init__(self, nomeUniversidade):
		self.nome_Estabelecimento = nomeUniversidade

class Unidade_Organica(Base):
	__tablename__='Unidade_Organica'
	nome_Unidade = Column('nome_Unidade', String, primary_key=True)
	nome_Estabelecimento = Column( String, ForeignKey('Estabelecimento_Ensino.nome_Estabelecimento'))

	def __init__(self, nome_Unidade, nome_Estabelecimento):
		self.nome_Unidade = nome_Unidade
		self.nome_Estabelecimento = nome_Estabelecimento

class Curso(Base):
	__tablename__='Curso'
	nome_Curso = Column('nome_Curso', String, primary_key= True)
	nome_Unidade = Column( String, ForeignKey('Unidade_Organica.nome_Unidade'))
	nivel_curso = Column( 'nivel_curso', String)
	def __init__(self, nome_Curso, nome_Unidade, nivel_curso):
		self.nome_Curso = nome_Curso
		self.nome_Unidade = nome_Unidade
		self.nivel_curso = nivel_curso

class Ano(Base):
	__tablename__='Ano'
	nome_Curso = Column('nome_Curso',String, primary_key = True)
	ano = Column('ano', String, primary_key = True)
	numero_alunos = Column('numero_alunos', Float)

	def __init__(self, nome_Curso, numero_alunos, ano ):
		self.nome_Curso = nome_Curso
		self.ano = ano
		self.numero_alunos = numero_alunos

Base.metadata.create_all()


def insertBD_Curso(nome_Estabelecimento, nome_Unidade, nome_Curso, nivel_curso):
	
	from sqlalchemy.orm import sessionmaker
	Session = sessionmaker(bind=engine)
	s = Session()
	s.add(Estabelecimento_Ensino(nome_Estabelecimento))
	s.add(Unidade_Organica(nome_Unidade, nome_Estabelecimento))
	s.add(Curso(nome_Curso, nome_Unidade, nivel_curso))
	try:
		s.commit()
	except IntegrityError:
		print 'ERROR'
		s.abort()

	

def com():
	s.commit()