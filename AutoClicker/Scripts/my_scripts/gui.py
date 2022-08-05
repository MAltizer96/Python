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
        self.geometry("200x200")

        # create start and stop jumping buttons
        self.startJumpButton = tk.Button(self,text="AutoJump",command=lambda : self.startAutoJump()) 
        self.stopJumpButton = tk.Button(self,text="Stop Jumping", command=lambda : self.stopAutoJump())

        # create start and stop clicking button
        self.startClickingButton = tk.Button(self,text="AutoClick",command=lambda : self.startAutoClicking())
        self.stopClickingButton = tk.Button(self,text="Stop Clicking", command=lambda : self.stopAutoClicking())

        # set places on grid for buttons
        self.startJumpButton.grid(column=1, row=0)
        self.stopJumpButton.grid(column=2,row=0)        
        self.startClickingButton.grid(column=1, row=1)
        self.stopClickingButton.grid(column=2,row=1)
          
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
        
