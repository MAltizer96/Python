
import tkinter as tk
from tkinter import ttk
from unicodedata import name

class gui(tk.Frame):
    def __init__(self, parent):
        #tk.Tk.__init__(self)
        super().__init__(parent)
        self.controller = None               
        self.initUI()

    def setController(self,controller):
        self.controller = controller

    def initUI(self): 
        self.initWidgets()

    def initWidgets(self):
        #self.createClickButton = tk.Button(self, text="Create Auto Click For Key", command=lambda : self.startAutoJump())
        # base ui
        self.initClickerWidgets()  
        self.initJumperWidgets()      

    def initClickerWidgets(self):  
        self.clickOnLabel = ttk.Label(self,text="Off",name="clickStatusLabel")
        self.clickOnLabel.grid(row=0,column=1)  

        self.clickButton = ttk.Button(self,text="AutoClick",command=lambda t="clickButton": self.changeButtonState(t,str(self.clickOnLabel)))    
        self.clickButton.grid(row=0,column=0)    
        
        self.clickDelayEntry = tk.Entry(self,width=5)
        self.clickDelayEntry.grid(row=0,column=2)

        self.currentClickerDelay = ttk.Label(self,text="1",name="clickerDelayLabel")
        self.currentClickerDelay.grid(row=0,column=4)

        self.delayClickEntryConfimButton = ttk.Button(self,text="Confirm",command=lambda t="clickButton": self.changeSpeeds(t,self.clickDelayEntry.get(),str(self.currentClickerDelay)))
        self.delayClickEntryConfimButton.grid(row=0,column=3)
        


    def initJumperWidgets(self):
        self.jumpOnLabel = ttk.Label(self,text="Off",name="jumpLabel")
        self.jumpOnLabel.grid(row=1,column=1)

        self.jumpButton = ttk.Button(self,text="AutoJump",command=lambda t="jumpButton": self.changeButtonState(t,str(self.jumpOnLabel)))
        self.jumpButton.grid(row=1,column=0)

        self.jumpDelayEntry = ttk.Entry(self,width=5)
        self.jumpDelayEntry.grid(row=1,column=2)

        self.currentJumpDelay = ttk.Label(self,text="1",name="jumpDelayLabel")
        self.currentJumpDelay.grid(row=1,column=4)
        
        self.delayJumpEntryConfirmButton = ttk.Button(self,text="Confirm",command=lambda t="jumpButton": self.changeSpeeds(t,self.jumpDelayEntry.get(),str(self.currentJumpDelay)))
        self.delayJumpEntryConfirmButton.grid(row=1,column=3)
    
    def changeButtonState(self,button,label):
        # Verify the controller is set
        if self.controller != None:
            # change state of thread
            self.controller.changeThreadState(button)
            if self.nametowidget(label).cget("text") == "Off":
                value = "On"
            else:
                value = "Off"
            self.changeLabelState(label,value)

    def changeSpeeds(self,button,value,label):
        # changes the delay speed on the button and updates the label to show new value
        print("base value: {}",value)
        self.controller.changeDelaySpeed(button,value)
        self.changeLabelState(label,value)


    def changeLabelState(self,labelName,value):
        print("labelName: {} value: {}",labelName,value)
        # changes the on or off switch next to button
        self.nametowidget(labelName).config(text=value)
        
    
    

        




    


