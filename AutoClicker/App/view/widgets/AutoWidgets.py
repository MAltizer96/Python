import tkinter as tk
class AutoWidgets(tk.Frame):
    def __init__(self,root,row,column,name):
        super().__init__(root)
        self.root = root  
        self.row = row
        self.name = name
        self.column = column
        self.controller = None        

    def set_controller(self, controller):
        self.controller = controller            

    def init_widgets(self):  
        # create button to start action
        clickButton = tk.Button(self.root,text="Auto"+self.name,command=lambda t=self.name + 'Button': self.changeButtonState(t,str(clickOnLabel)))    
        # set place for button
        clickButton.grid(row=self.row,column=self.column)

        # create label for to tell if action is on
        clickOnLabel = tk.Label(self.root,text="Off",name=self.name + 'Label')
        # set place for label
        clickOnLabel.grid(row=self.row,column=self.column + 1)

        # created Entry field to take in user input for changing speed of action
        clickDelayEntry = tk.Entry(self.root,width=5)
        # set place for entry
        clickDelayEntry.grid(row=self.row,column=self.column + 2)

        # create button for confirming changing speed of action, using input form the entry field
        delayClickEntryConfimButton = tk.Button(self.root,text="Confirm",command=lambda t=self.name + 'Button': self.changeSpeeds(t,clickDelayEntry.get(),str(currentClickerDelay)))
        # set place for confirm cuttong
        delayClickEntryConfimButton.grid(row=self.row,column=self.column + 3)

        # create a label to display what the current speed of action if, default is set to 1
        currentClickerDelay = tk.Label(self.root,text="1",name=self.name+'DelayLabel')
        # set place for label
        currentClickerDelay.grid(row=self.row,column=self.column + 4)



    def changeSpeeds(self,button,value,label):
        # takes in the string of the button which of clicked
        # value as a string to change the speed to
        # label as a string to update the displayed value

        # checks for controller      
        if self.controller != None:                                
            # changed the speed of the action
            self.controller.changeValues(button,value)
            # updates the label with the new value
            self.changeLabelState(label,value)
        else:
            print('need controller')
   

    def changeButtonState(self,button,label):
        # takes in the string of the button which of clicked
        # label as a string to update the displayed value

        # Verify the controller is set        
        if self.controller != None:
            # change state of thread
            self.controller.changeThreadState(button)
            # changes the display value for the widget to show if its off or on
            if self.nametowidget(label).cget("text") == "Off":
                value = "On"
            else:
                value = "Off"
            self.changeLabelState(label,value)

    def changeLabelState(self,labelName,value):        
        # changes the on or off switch next to button
        self.nametowidget(labelName).config(text=value) 

        
        
