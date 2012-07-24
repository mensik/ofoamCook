import wx

class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'oFoamCook')
        
        self.CreateStatusBar()
        
        filemenu = wx.Menu()
        menuItem = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, menuItem)
        
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        
        self.SetMenuBar(menuBar)
        
        
        self.Show()
        
    def OnAbout(self, event):
        print 'ABOUT'

app = wx.App()

frame = MainWindow()
app.MainLoop()