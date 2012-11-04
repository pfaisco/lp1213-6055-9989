# -*- coding: utf-8 -*-
import sqlite3
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, DateTime, Time, Float, ForeignKey
from sqlalchemy.orm import mapper, create_session, sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
#def cria_Base_Dado():
#pass



def createDB(nome_bd = 'inscricoes.db'):
	file = open(nome_bd , 'w')
	file.write('')
	file.close()
	conn = sqlite3.connect(nome_bd)
	cursor = conn.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS Cursos (
		NomeCurso TEXT PRIMARY KEY, 
		Universidade TEXT, 
		Faculdade TEXT, 
		Nivel TEXT)''')
	cursor.execute('''CREATE TABLE IF NOT EXISTS Contagens (
		AnoLectivo TEXT, 
		NomeCurso TEXT,
		NumeroAlunos INTEGER, 
		FOREIGN KEY(NomeCurso) REFERENCES Cursos(NomeCurso), 
		PRIMARY KEY(AnoLectivo, NomeCurso))''')
	conn.commit()
	cursor.close()
	pass

createDB('pedro.db')	

dbEngine = create_engine('mysql://root:admin@192.168.233.128/simoc_testing', echo = True)
Base = declarative_base(bind = dbEngine)



class Establecimento(Base):
'''

'''
__tablename__='Establecimento'
id = Column('id', Integer, 	primary_key=True)
nomeEstablecimmento
def __init__(self, nomeEstablecimmento):
	Column





