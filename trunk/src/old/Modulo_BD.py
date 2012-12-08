# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Float, String, ForeignKey, Integer, distinct, func
from sqlalchemy.orm import relationship, backref, query

#if __name__ == '__main__':				
engine = create_engine('sqlite:///./basedado.db', echo = True)
Base = declarative_base(bind = engine)
#	Base.metadata.create_all()
#	print 'DONE!!!'

class BaseDado():
	def __init__():
		pass
	pass



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
		return 'Ano : {0}, Alunos: {1}'.format(self.ano, self.numero_alunos)

	
		

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
##################################################################
#
#		QUERY
#
##################################################################
def query_nome_cursos():
	"""
		Metodo Query Lista de Cursos
	"""
	s = create_session()
	l = s.query(Curso).all()
	return l



def query_Curso(show_all = True, total = False):
	"""
		Anos em que os cursos estiveram em funcionamento
	"""
	s = create_session()
	q_c = query_nome_cursos()
	res=[]
	for c in q_c:
		curso_info=[]
		curso_info.append(c.nome_Curso.encode('utf-8'))
		curso_info.append(c.nome_Estabelecimento.encode('utf-8'))
		curso_info.append(c.nome_Unidade.encode('utf-8'))
		curso_info.append(c.nivel_Curso.encode('utf-8'))

		x = s.query(Ano).filter(Ano.id_Curso == c.id).all()
	
		for a in x:
			if a.numero_alunos > 0:   #condiçao para graficos not_exists
				curso_info.append(a.ano)
		res.append(curso_info)
	return res

def query_contagem_niveis():
	"""
		Contagem de alunos por nivel ano
	"""
	s = create_session()
	cont = s.query(Curso.nivel_Curso, Ano.ano, func.sum(Ano.numero_alunos)).join(Ano).filter(Curso.id == Ano.id_Curso).group_by(Curso.nivel_Curso, Ano.ano).all()
	res=[]

	for i in cont:
		res.append((i[0].encode('utf-8'),i[1], i[2]))
	return res

def query_contagem_Curso_alunos():
	"""
		Contagem de alunos por curso ano
	"""
	s = create_session()
	cont = s.query(Curso.nome_Curso, Ano.ano, func.sum(Ano.numero_alunos)).join(Ano).filter(Curso.id == Ano.id_Curso).group_by(Curso.id, Ano.ano).all()
	res=[]
	for i in cont:
		res.append((i[0].encode('utf-8'),i[1], i[2]))
	return res	
	
def query_contagem_nivel_curso():
	"""
		Contagem de cursos por nivel ano
		select Curso.nivel_curso , ano.ano, count( curso.id )
			from Curso  join ano where curso.id == id_curso 
			group by  ano.ano, curso.nome_curso;
	"""
	s = create_session()
	cont = s.query(Curso.nivel_Curso, Ano.ano, func.count(Curso.id)).join(Ano).filter(Curso.id == Ano.id_Curso).group_by(Ano.ano, Curso.nome_Curso).all()
	res=[]
	for i in cont:
		res.append((i[0].encode('utf-8'),i[1], i[2]))
	return res	
	

def query_contagem(query_ans):
	'''
		nao utilizado
	'''
	s = create_session()
	#q1 = 
	q = s.query(Ano).filter(Ano.id_Curso == c.id_Curso).all()

def qnt_alunos(show_all = True, not_exits = False):
	"""
		Não utilizado, só para teste
	"""
	s = create_session()
	c = query_nome_cursos()
	
	for y in c:
		total = 0
		print y
		x = s.query(Ano).filter(Ano.id_Curso == y.id).all()
		for a in x:
			if show_all:
				print a   ###########################################################
			total += a.numero_alunos
		print 'Total: {0}'.format(total)
		print '\n'



# 	nomeBD = 'sqlite:///./basedado.db'
# 	engine = create_engine(nomeBD, echo = True)
	# Base = declarative_base(bind = engine)

'''
	O codigo dentro do if so é executado quando 
	é chamado este modolo, não quando é evocado por outros modulos
'''
if __name__ == '__main__':	
	Base.metadata.create_all()

	#printBD()

'''
tirar o echo nas query
e modificar o create bd para um metodo # if __name__ == '__main__':
'''