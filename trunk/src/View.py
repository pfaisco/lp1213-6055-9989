#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.5 on Thu Dec  6 23:30:41 2012
from Controller_DB import Controller_DB
import wx

# begin wxGlade: extracode
# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        cdb = Controller_DB()

        self.lst_cmb_CSV = ['anos letivos em que funcionaram cursos que incluem o termo computadores e informática',
                    'quantidade de alunos que nestes se inscreveram ao longo dos anos',
                    'quantidade de cursos por nível de formação ao longo dos anos',
                    'quantidade de alunos por nível de formação ao longo dos anos']
        try:
            self.lst_cmb_Major = cdb.query_major() 
            self.lst_cmb_Degree = cdb.query_degree()
        except:
            self.lst_cmb_Major = []
            self.lst_cmb_Degree = []
            print 'No such table!'
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.btnMakeDB = wx.Button(self, -1, "Import Data to Database")
        self.CSV = wx.StaticText(self, -1, "CSV")
        self.cmbCSV = wx.ComboBox(self, -1, choices=self.lst_cmb_CSV, style=wx.CB_READONLY)
        self.btnCSV = wx.Button(self, -1, "Write")
        self.Plot = wx.StaticText(self, -1, "Plot")
        self.cmbMajor = wx.ComboBox(self, -1, choices=self.lst_cmb_Major, style=wx.CB_READONLY)
        self.btnPlotMajor = wx.Button(self, -1, "Plot")
        self.cmbDegree = wx.ComboBox(self, -1, choices=self.lst_cmb_Degree, style=wx.CB_READONLY)
        self.btnPlotDegree = wx.Button(self, -1, "Plot")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("lp1213_6055_9989")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(7, 2, 10, 10)
        grid_sizer_1.Add(self.btnMakeDB, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.CSV, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.cmbCSV, 0, 0, 0)
        grid_sizer_1.Add(self.btnCSV, 0, 0, 0)
        grid_sizer_1.Add(self.Plot, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.cmbMajor, 0, 0, 0)
        grid_sizer_1.Add(self.btnPlotMajor, 0, 0, 0)
        grid_sizer_1.Add(self.cmbDegree, 0, 0, 0)
        grid_sizer_1.Add(self.btnPlotDegree, 0, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.ALL | wx.EXPAND, 15)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade
# end of class MainFrame

# end of class MyMenuBar

# if __name__ == "__main__":
#     class AppView(wx.App):
#         def OnInit(self):
#             wx.InitAllImageHandlers()
#             frame_1 = MainFrame(None, -1, "")
#             self.SetTopWindow(frame_1)
#             frame_1.Show()
#             return 1

# # end of class AppView

#     lp1213_6055_9989 = AppView(0)
#     lp1213_6055_9989.MainLoop()
