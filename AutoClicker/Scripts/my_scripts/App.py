import tkinter as tk
from new_gui import gui
from Controller import Controller
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AutoClickerApp")               
        self.geometry("250x150")
        view = gui(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        controller = Controller(view)

        view.setController(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
        