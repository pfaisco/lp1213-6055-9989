# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Float, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref, query

engine = create_engine('sqlite:///./basedado.db', echo = True)
Base = declarative_base(bind = engine)

def criaMotor(self, nome='basedado.db'):
	'''
	nome: nome do ficheiro da base dados
	cria Motor da base de dados para ligar e criar as tabelas e as seçoes
	'''
	if nome.endswith('.db'):
		nome.join('.db')
		pass

	nomeBD = 'sqlite:///' + nome 
	engine = create_engine(nomeBD, echo = True)
	Base = declarative_base(bind = engine)
	pass




class Curso(Base):
	'''

	'''
	__tablename__='Curso'
	id = Column(Integer, primary_key = True)
	nome_Curso = Column('nome_Curso', String)
	nome_Unidade = Column('nome_Unidade', String)
	nome_Estabelecimento = Column('nome_Estabelecimento', String)
	nivel_Curso = Column( 'nivel_Curso', String)
	

	def __init__(self, nome_Curso, nome_Unidade, nivel_curso, nome_Estabelecimento):
		self.nome_Curso = nome_Curso
		self.nome_Unidade = nome_Unidade
		self.nome_Estabelecimento = nome_Estabelecimento
		self.nivel_Curso = nivel_curso
	
	def __repr__(self):
		r = "Curso: {0} \nUnidade: {1} \nEstabelecimento {2} \nNivel {3}".format(self.nome_Curso.encode('utf-8'), self.nome_Unidade.encode('utf-8'), self.nome_Estabelecimento.encode('utf-8'), self.nivel_Curso.encode('utf-8'))
		return r

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

	def __repr__(self):
		return 'ano : {0} -> {1}'.format(self.ano, self.numero_alunos)

	
		

def insertBD_Curso(nome_Estabelecimento, nome_Unidade, nome_Curso, nivel_curso, l_anos):
	s = create_session()
	c = Curso(nome_Curso = nome_Curso, nome_Unidade = nome_Unidade, nivel_curso = nivel_curso, nome_Estabelecimento= nome_Estabelecimento)
	for a in l_anos:
		c.Ano.extend([Ano(ano_c=a[0], numero_alunos=a[1])])
	s.add(c)
	
	try:
		s.commit()
	except:
		print 'ERROR_Commit'


def create_session():
	from sqlalchemy.orm import sessionmaker
	
	engine = create_engine('sqlite:///./basedado.db', echo = False)

	Session = sessionmaker(bind = engine)
	s = Session()
	return s
	

def query_nome_cursos():
	"""
	Metodo Query Lista de Cursos
	"""
	s = create_session()
	l = s.query(Curso).all()
	for y in l:
		print y.nome_Curso 

def qnt_alunos():
	"""

	"""
	s = create_session()
	c = s.query(Curso)
	
	for y in c:
		total = 0
		print y
		x = s.query(Ano).filter(Ano.id_Curso == y.id).all()
		for a in x:
			print a
			total += a.numero_alunos
		print 'Total: {0}'.format(total)
		print '\n'
def nivel():
	"""

	"""
	s = create_session()
	c = s.query(Curso.nivel_Curso)
	
	for y in c:		
		print y


# if __name__ == '__main__':				
# 	nomeBD = 'sqlite:///./basedado.db'
# 	engine = create_engine(nomeBD, echo = True)
	# Base = declarative_base(bind = engine)
Base.metadata.create_all()
print 'DONE!!!'
	#Base.metadata.create_all()

	#printBD()

'''
tirar o echo nas query
e modificar o create bd para um metodo # if __name__ == '__main__':
'''