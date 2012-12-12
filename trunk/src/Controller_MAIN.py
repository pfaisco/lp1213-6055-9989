#-*- coding: utf-8 -*-
from Controller_Xls import Controller_Xls
from Controller_DB import Controller_DB
from Model_csv import Controller_stat
from Model_plot import Controller_Plot
import sys
from View import MainFrame
import wx
import time

from threading import Thread


 



"""
	Control the main of the of application and launch the view
"""

	
def make_DB( event):
	"""
		Create Database when the buttun is clicked
	"""
	start_time = time.time()
	c_D = Controller_DB()
	c_D.create_db()
	c_xls = Controller_Xls()
	lista = c_xls.read_xls()
	for l in lista:
		c_D.insertBD_Major(name_University=l[1], name_School=l[2], name_Major=l[0], degree=l[3], l_Years=l[4])
	print time.time() - start_time, "seconds"
	
def make_csv( event, cmbox):
	"""
		Receicves data from main window to make csv file
		and create it
	"""
	start_time = time.time()
	C_D = Controller_DB()
	query = cmbox.GetCurrentSelection()
	if query == 0:
		l = C_D.query_major_funcionamento()
		C_S = Controller_stat('q1.csv')
		C_S.write_to_csv(l)
	elif query == 1:
		l = C_D.query_students_degrees()
		C_S = Controller_stat('q2.csv')
		C_S.write_to_csv(l)
	elif query == 2:
		l = C_D.query_students_major()
		C_S = Controller_stat('q3.csv')
		C_S.write_to_csv(l)
	elif query == 3:
		l = C_D.query_major_degree()
		C_S = Controller_stat('q4.csv')
		C_S.write_to_csv(l)
	print time.time() - start_time, "seconds"

def plot_major( event, cmbox ):
	"""
		Plot the info about the major selected on combobox
	"""
	start_time = time.time()
	id_major = cmbox.GetCurrentSelection()
	name = cmbox.GetStringSelection()
	
	id_major = id_major + 1
	
	C_D = Controller_DB()
	lista = C_D.query_students_major_plot(id_major)

	x=[]
	y=[]
	for i in lista:
		x.append(i[1])
		y.append(i[2])
	
	C_p = Controller_Plot(name ,x, y)
	
	C_p.plot_data()
	print time.time() - start_time, "seconds"
	pass

def plot_degree( event, cmbox ):
	"""
		Plot the info about the degree selected on combobox
	"""
	start_time = time.time()
	

	sel = cmbox.GetStringSelection()
	title = sel.split(' | ')
	if sel != '':
		C_D = Controller_DB()
		lista = C_D.query_students_degrees()
		x=[]
		y=[]

		for i in lista:
		
			if i[0].find(sel.encode('utf-8')) >= 0:
				x.append(i[1])
				y.append(i[2])
		C_p = Controller_Plot(title[0],x, y)
		C_p.plot_data()
	print time.time() - start_time, "seconds"
	pass


if __name__ == "__main__":
	class AppView(wx.App):
		def OnInit(self):
			
			
			wx.InitAllImageHandlers()
			frame_1 = MainFrame(None, -1, "")
			frame_1.btnMakeDB.Bind(wx.EVT_BUTTON, lambda event:make_DB(event), frame_1.btnMakeDB)
			frame_1.btnCSV.Bind(wx.EVT_BUTTON, lambda event, cmb = frame_1.cmbCSV: Thread( target = make_csv, args = (event, cmb,)), frame_1.btnCSV)
			
			frame_1.btnPlotMajor.Bind(wx.EVT_BUTTON, lambda event, cmb = frame_1.cmbMajor:Thread( target = plot_major, args = ( event,cmb, ) ).start(), frame_1.btnPlotMajor)

			
			frame_1.btnPlotDegree.Bind(wx.EVT_BUTTON, lambda event, cmb = frame_1.cmbDegree: Thread( target = plot_degree, args = ( event,cmb, ) ).start(), frame_1.btnPlotDegree)	
			self.SetTopWindow(frame_1)
			frame_1.Show()
			return 1

# end of class AppView
	
	lp1213_6055_9989 = AppView(0)
	

	Thread( target=lp1213_6055_9989.MainLoop()).start()
	
