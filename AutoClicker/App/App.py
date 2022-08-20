import tkinter as tk
from new_gui import gui
from Controller import Controller
from AutoClick import PushMouseButton
from AutoJump import PushButtons
from HotKeys import HotKeys

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AutoClickerApp")               
        self.geometry("250x150")

        view = gui(self)               
        view.grid(row=0, column=0, padx=10, pady=10)        
  
        self.autoClicker = PushMouseButton()
        self.autoJump = PushButtons()
        self.hotkey = HotKeys()
        
        self.autoJump.start()
        self.autoClicker.start()
        self.hotkey.start()

        model = [self.autoClicker,self.autoJump,self.hotkey]
        controller = Controller(view,model)
        view.setController(controller)
        self.hotkey.setController(controller)
    
    def stopProgram(self):
        self.autoClicker.stop()
        self.autoJump.stop()     
        self.hotkey.stop()  



if __name__ == '__main__':
    app = App()
    app.mainloop()
    app.stopProgram()
        