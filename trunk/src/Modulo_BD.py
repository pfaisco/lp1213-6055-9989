# -*- coding: utf-8 -*-
import sqlite3

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