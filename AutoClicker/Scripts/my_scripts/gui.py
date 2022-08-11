import tkinter as tk
from threading import Thread
from pynput.keyboard import Listener,KeyCode
from tkinter.ttk import Frame 
from pynput import mouse, keyboard
from AutoJump import PushButtons
from AutoClick import PushMouseButton

autoJump = PushButtons()
autoClick = PushMouseButton()
class gui(tk.Tk):
    def __init__(self):            
        tk.Tk.__init__(self)
        self.initUI()
        
        #myButton.start()#

    def initUI(self):        
        self.title("AutoClickerApp")               
        self.geometry("250x150")

        # create start and stop jumping buttons
        self.startJumpButton = tk.Button(self,text="AutoJump",command=lambda : self.startAutoJump()) 
        self.stopJumpButton = tk.Button(self,text="Stop Jumping", command=lambda : self.stopAutoJump())
        self.autoJumpDelayText = tk.Entry()
        self.changeJumpDelayButton = tk.Button(self,text="Auto Jump delay",command=lambda :  self.setAutoJumpDelayValue(self.autoJumpDelayText))
        self.currentJumpDelay = tk.Label()

        # create start and stop clicking button
        self.startClickingButton = tk.Button(self,text="AutoClick",command=lambda : self.startAutoClicking())
        self.stopClickingButton = tk.Button(self,text="Stop Clicking", command=lambda : self.stopAutoClicking())
        self.autoClickDelayText = tk.Entry()
        self.changeClickDelayButton = tk.Button(self,text="Auto Click delay",command=lambda :  self.setAutoClickDelayValue(self.autoClickDelayText))
        self.currentClickDelay = tk.Label()
        
        # set places on grid for buttons
        self.startJumpButton.grid(column=1, row=0)
        self.stopJumpButton.grid(column=2,row=0)   
        self.autoJumpDelayText.grid(column=1,row=1)
        self.changeJumpDelayButton.grid(column=2,row=1)
        self.currentJumpDelay.grid(column=3,row=1)

        self.startClickingButton.grid(column=1, row=2)
        self.stopClickingButton.grid(column=2,row=2)
        self.autoClickDelayText.grid(column=1,row=3)
        self.changeClickDelayButton.grid(column=2,row=3)
        self.currentClickDelay.grid(column=3,row=3)
        
          
    def setAutoJumpDelayValue(self, entry):
        value = entry.get()
        #setValuehere   

        autoJump.delay = float(value)
        self.currentJumpDelay.config(text=float(value))
        
    def setAutoClickDelayValue(self, entry):
        value = entry.get()
        autoClick.delay = float(value)
        self.currentClickDelay.config(text=float(value))

    def startAutoJump(self):       
       autoJump.startJumping()
       # checks if thread is already made
       if autoJump.is_alive() == False:
            autoJump.start()

    def stopAutoJump(self):
        autoJump.stopJumping()

    def startAutoClicking(self):
        autoClick.startClicking()
        # checks if thread is already made
        if autoClick.is_alive() == False:
            autoClick.start()

    def stopAutoClicking(self):
        autoClick.stopClicking()

    def stopProgram(self):
        autoJump.stop()
        autoClick.stop()
        
