# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Float, String, Integer, distinct, func
from sqlalchemy.orm import query, sessionmaker
from Model_DB import Major, Year, modelDB
import os

class Controller_DB(modelDB):
	"""
	Class Controller_DB Being part of MVC architechture has the 
	Methods to control functions related with Database
	"""
	def create_db(self):
		"""
		Call Module_DB to create the Database file with the tabels
		"""
		os.system('python Model_DB.py')


	def insertBD_Major(self, name_University, name_School, name_Major, degree, l_Years):
		"""
		Insert tuples at database

		"""
		s = self.create_session()
		c = Major(name_Major = name_Major, name_School = name_School, degree = degree, name_University= name_University)
		for a in l_Years:
			c.Year.extend([Year(Year_c=a[0], number_students=a[1])])
		s.add(c)
		s.commit()
		try:
			s.commit()
		except:
			print 'ERROR_Commit'

	def create_session(self):
		"""
		Create a sessoin with sqlalchemy to connect with database to 
		query or insert data in Database
		"""
		Session = sessionmaker(bind = self.engine)
		s = Session()
		return s

	##################################################################
	#
	#		QUERY
	#
	##################################################################
	def query_majors_info(self):
		"""
			Do query to database returning info about Major

		"""
		s = self.create_session()
		l = s.query(Major).all()
		return l
	
	def query_major(self):
		"""
			Query database returning Major Name, university and degree
		"""
		s = self.create_session()
		l = s.query(Major.name_Major, Major.name_University, Major.degree_Major).all()
		res = []
		for i in l:
			s = i[0] + ' | ' + i[1] + ' | ' + i[2]
			res.append(s)

		return res

	def query_degree(self):
		"""
			Query return a list of all degrees without repeting
		"""
		s = self.create_session()
		l = s.query(distinct(Major.degree_Major)).all()
		res = []
		for i in l:
			res.append(i[0])
		return res

	def query_major_funcionamento(self):
		"""
			Years when the courses were working
		"""
		s = self.create_session()
		q_c = self.query_majors_info()
		res=[]
		for c in q_c:
			major_info=[]
			major_info.append(c.name_Major.encode('utf-8'))
			major_info.append(c.name_University.encode('utf-8'))
			major_info.append(c.name_School.encode('utf-8'))
			major_info.append(c.degree_Major.encode('utf-8'))

			x = s.query(Year).filter(Year.id_Major == c.id).all()
		
			for a in x:
				if a.number_students > 0:   
					major_info.append(a.Year)
			res.append(major_info)
		return res

	def query_students_niveis(self, degree = None):
		"""
			
		"""
		s = self.create_session()
	
		cont = s.query(Major.degree_Major, Year.Year, func.sum(Year.number_students)).join(Year).filter(Major.id == Year.id_Major).group_by(Major.degree_Major, Year.Year).all()
		res=[]
		for i in cont:
			res.append((i[0].encode('utf-8'),i[1], i[2]))
		return res
		

	def query_students_major(self):
		"""
			Contagem de students por major Year
		"""
		s = self.create_session()
		cont = s.query(Major.name_Major, Year.Year, func.sum(Year.number_students)).join(Year).filter(Major.id == Year.id_Major).group_by(Major.id, Year.Year).all()
		res=[]
		for i in cont:
			res.append((i[0].encode('utf-8'),i[1], i[2]))
		return res	
		
	def query_major_degree(self):
		"""
			Contagem de majors por degree Year
			select Major.degree , Year.Year, count( major.id )
				from Major  join Year where major.id == id_major 
				group by  Year.Year, major.name_major;
		"""
		s = self.create_session()
		cont = s.query(Major.degree_Major, Year.Year, func.count(Major.id)).join(Year).filter(Major.id == Year.id_Major).group_by(Year.Year, Major.name_Major).all()
		res=[]
		for i in cont:
			res.append((i[0].encode('utf-8'),i[1], i[2]))
		return res	
	def query_students_major_plot(self, id_Major):
		"""
			Contagem de students por major Year  
		"""
		s = self.create_session()
		cont = s.query(Major.name_Major, Year.Year, func.sum(Year.number_students)).join(Year).filter(Major.id == id_Major).group_by(Major.id, Year.Year).all()
		res=[]
		for i in cont:
			res.append((i[0].encode('utf-8'),i[1], i[2]))
		return res	
	