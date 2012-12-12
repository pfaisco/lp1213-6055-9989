# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Float, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref

class Model_DB(object):
	"""
		Class Model_DB 
	"""
	
	def __init__(self, name = 'sqlite:///./basedados.db'):
		"""
			Contructor of class Model_DB when an instance of this class is created
			create a Base and an engine to connect to Database
		"""
		self.engine = create_engine(name, echo = False)
		self.Base = declarative_base(bind = self.engine)
		
		
m = Model_DB()
Base = m.Base

class Major(Base):
	"""
		Class of table Major to sqlalchemy with info about 
		Majors
	"""
	__tablename__='Major'
	id = Column(Integer, primary_key = True)
	name_Major = Column('name_Major', String)
	name_School = Column('name_School', String)
	name_University = Column('name_University', String)
	degree_Major = Column( 'degree_Major', String)
	
	def __init__(self, name_Major, name_School, degree, name_University):
		"""
			Constructor of class tabel Major
		"""
		self.name_Major = name_Major
		self.name_School = name_School
		self.name_University = name_University
		self.degree_Major = degree
	
class Year(Base):
	"""
		Class of table Year to sqlalchemy containing info about 
		each major of each year
	"""
	__tablename__='Year'
	id=Column(Integer, primary_key=True)
	Year = Column('Year', String)
	number_students = Column('number_students', Float)
	major = relationship("Major", backref=backref("Year"))
	id_Major = Column(Integer, ForeignKey('Major.id'))
	
	def __init__(self, number_students, Year_c ):
		"""
			Constructor of class table Year
		"""
		self.Year = Year_c
		self.number_students = number_students

if __name__ == '__main__':
	m.Base.metadata.create_all()
