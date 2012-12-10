#-*- coding: utf-8 -*-
from Controller_Xls import Controller_Xls
from Controller_DB import Controller_DB
from Model_csv import Controller_stat
from Model_plot import Controller_Plot
import sys
from View import MainFrame

import wx

class Controller_Main(object):
	
	
	def make_DB(self, event):
		c_D = Controller_DB()
		c_D.create_db()
		c_xls = Controller_Xls()
		lista = c_xls.read_xls()
		for l in lista:
			c_D.insertBD_Major(name_University=l[1], name_School=l[2], name_Major=l[0], degree=l[3], l_Years=l[4])
		
	def make_csv(self, event, cmbox):
		C_D = Controller_DB()
		query = cmbox.GetCurrentSelection()
		if query == 0:
			l = C_D.query_major_funcionamento()
			C_S = Controller_stat('q1.csv')
			C_S.write_to_csv(l)
		elif query == 1:
			l = C_D.query_students_niveis()
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

	def plot_major(self, event, cmbox ):
		id_major = cmbox.GetCurrentSelection()
		name = cmbox.GetStringSelection()
		"""		name.replace(' | ', '\n')
		"""	
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
		pass

	def plot_degree(self, event, cmbox ):
		sel = cmbox.GetStringSelection()
		
		C_D = Controller_DB()
		lista = C_D.query_students_niveis()
		x=[]
		y=[]

		for i in lista:
			
			if i[0].find(sel.encode('utf-8')) >= 0:
				x.append(i[1])
				y.append(i[2])
		C_p = Controller_Plot(sel,x, y)
		C_p.plot_data()
		pass




if __name__ == "__main__":
	class AppView(wx.App):
		def OnInit(self):

			wx.InitAllImageHandlers()
			frame_1 = MainFrame(None, -1, "")
			Cm = Controller_Main()
			frame_1.btnMakeDB.Bind(wx.EVT_BUTTON, Cm.make_DB, frame_1.btnMakeDB)
			frame_1.btnCSV.Bind(wx.EVT_BUTTON, lambda event, cmb = frame_1.cmbCSV: Cm.make_csv(event, cmb), frame_1.btnCSV)
			frame_1.btnPlotMajor.Bind(wx.EVT_BUTTON, lambda event, cmb = frame_1.cmbMajor: Cm.plot_major(event, cmb), frame_1.btnPlotMajor)
			frame_1.btnPlotDegree.Bind(wx.EVT_BUTTON, lambda event, cmb = frame_1.cmbDegree: Cm.plot_degree(event, cmb), frame_1.btnPlotDegree)	
			self.SetTopWindow(frame_1)
			frame_1.Show()
			return 1

# end of class AppView

	lp1213_6055_9989 = AppView(0)
	lp1213_6055_9989.MainLoop()
