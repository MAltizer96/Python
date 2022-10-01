import tkinter as tk
from view.new_gui import gui
from controller.Controller import Controller
from model import AutoJump,AutoClick,HotKeys,ScanGui

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # set title and size of app window
        self.title("AutoClickerApp")               
        self.geometry("250x150")
        # set the view
        view = gui(self)
        # set padding               
        view.grid(row=0, column=0, padx=10, pady=10)        
        # create model objects
        self.autoClicker = AutoClick.PushMouseButton()
        self.autoJump = AutoJump.PushButtons()
        self.hotkey = HotKeys.HotKeys()
        self.scanGUI = ScanGui.ScanGui()
        # start threads
        self.autoJump.start()
        self.autoClicker.start()
        self.hotkey.start()
        self.scanGUI.start()
        # set model in a list
        model = [self.autoClicker,self.autoJump,self.hotkey,self.scanGUI]
        # make controlle with model and view
        controller = Controller(view,model)
        # set the controller for the view
        view.set_controller(controller)
        # set controller for hotkeys model
        self.hotkey.setController(controller)

        #view.pack()
    
    def stopProgram(self):
        self.autoClicker.stop()
        self.autoJump.stop()     
        self.hotkey.stop() 
        self.scanGUI.stop() 



if __name__ == '__main__':
    app = App()
    app.mainloop()
    app.stopProgram()
        