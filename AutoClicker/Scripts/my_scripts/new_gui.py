import tkinter as tk
from Controller import Controller
class gui(tk.Frame):
    def __init__(self, parent):
        #tk.Tk.__init__(self)
        super().__init__(parent)
        self.initUI()

    def setController(self,controller):
        self.controller = controller

    def initUI(self):
        self.jumpBool = tk.BooleanVar()
        self.spaceString = tk.StringVar()
        self.jumpBool.set=True
        self.spaceString.set = "space"
        self.initWidgets()

    def initWidgets(self):
        #self.createClickButton = tk.Button(self, text="Create Auto Click For Key", command=lambda : self.startAutoJump())
        # base ui
        self.initbaseUI()        

    
    def initbaseUI(self):
        self.jumpButton = tk.Button(self,text="AutoJump",command=self.jumpButtonClicked())
        self.clickButton = tk.Button(self,text="AutoClick",command=self.clickButtonClicked())

    def jumpButtonClicked(self):
        if self.controller:            
            self.controller.activateButton(self.jumpBool,self.spaceString)
            print("current jump bool: ", self.jumpBool)
            self.jumpBool != self.jumpBool
            print("after jump bool change: ", self.jumpBool)

    def clickButtonClicked(self):
        if self.controller:
            self.controller.activateButton()



