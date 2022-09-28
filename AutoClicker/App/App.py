import tkinter as tk
from view import new_gui
from controller import Controller
from model import AutoJump,AutoClick,HotKeys,ScanGui

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AutoClickerApp")               
        self.geometry("250x150")

        view = new_gui.gui(self)               
        view.grid(row=0, column=0, padx=10, pady=10)        
  
        self.autoClicker = AutoClick.PushMouseButton()
        self.autoJump = AutoJump.PushButtons()
        self.hotkey = HotKeys.HotKeys()
        self.scanGUI = ScanGui.ScanGui()

        self.autoJump.start()
        self.autoClicker.start()
        self.hotkey.start()
        self.scanGUI.start()

        model = [self.autoClicker,self.autoJump,self.hotkey,self.scanGUI]
        controller = Controller.Controller(view,model)
        view.setController(controller)
        self.hotkey.setController(controller)
    
    def stopProgram(self):
        self.autoClicker.stop()
        self.autoJump.stop()     
        self.hotkey.stop() 
        self.scanGUI.stop() 



if __name__ == '__main__':
    app = App()
    app.mainloop()
    app.stopProgram()
        