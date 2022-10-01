from tkinter import IntVar
import tkinter as tk
#from view.widgets.custom_widgets import initJumperWidgets, initScanWidgets
from view.widgets.AutoWidgets import AutoWidgets

class gui(tk.Frame):
    def __init__(self, parent, controller=None):
        #tk.Tk.__init__(self)
        super().__init__(parent)
        self.auto_clicker_widgets = AutoWidgets(parent,0,0,'click')
        self.auto_jump_widgets = AutoWidgets(parent,1,0,'jump')
        self.auto_scan_widgets = AutoWidgets(parent,2,0,'scan')
        self.controller = None               
        self.initUI()

    def set_controller(self,controller):
        self.controller = controller
        self.auto_clicker_widgets.set_controller(self.controller) 
        self.auto_jump_widgets.set_controller(self.controller)
        self.auto_scan_widgets.set_controller(self.controller)      
    
    def get_controller(self):
        return self.controller

    def initUI(self): 
        self.initWidgets()

    def initWidgets(self):        
        # creates widgets      
        self.auto_clicker_widgets.init_widgets()
        self.auto_jump_widgets.init_widgets()
        self.auto_scan_widgets.init_widgets()

    def changeNumberOfRows(self,button,rows,label):
        self.controller.changeScanRows(button,rows)
        self.changeLabelState(label,rows)


    
    def changeLabelStateOff(self):
        self.nametowidget("jumpLabel").config(text="Off")
        self.nametowidget("clickLabel").config(text="Off")
        self.nametowidget("scanLabel").config(text="Off")
    
    def changeMovement(self):        
        if self.moveCheck.get() == 0:
            self.controller.changeMovementState(False)
        else:
            self.controller.changeMovementState(True)

    def changeScanWidth(self):
        if self.halfScreenCheck.get() == 0:
            self.controller.changeScanWidth(False)
        else:
            self.controller.changeScanWidth(True)

       
    
    

        




    


