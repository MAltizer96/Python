from tkinter import ttk, IntVar

from view.widgets import custom_widgets

class gui(ttk.Frame):
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
        custom_widgets.initClickerWidgets(self)  
        custom_widgets.initJumperWidgets(self)
        custom_widgets.initScanWidgets(self)  
    

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
        #print("base value: {}",value)
        self.controller.changeDelaySpeed(button,value)
        self.changeLabelState(label,value)

    def changeNumberOfRows(self,button,rows,label):
        self.controller.changeScanRows(button,rows)
        self.changeLabelState(label,rows)

    def changeLabelState(self,labelName,value):
        #print("labelName: {} value: {}",labelName,value)
        # changes the on or off switch next to button
        self.nametowidget(labelName).config(text=value)
    
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

       
    
    

        




    


