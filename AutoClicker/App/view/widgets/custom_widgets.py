from tkinter import ttk, IntVar

def initClickerWidgets(root):  
    clickOnLabel = ttk.Label(root,text="Off",name="clickLabel")
    clickOnLabel.grid(row=0,column=1)  

    clickButton = ttk.Button(root,text="AutoClick",command=lambda t="clickButton": root.changeButtonState(t,str(root.clickOnLabel)))    
    clickButton.grid(row=0,column=0)    
    
    clickDelayEntry = ttk.Entry(root,width=5)
    clickDelayEntry.grid(row=0,column=2)

    currentClickerDelay = ttk.Label(root,text="1",name="clickerDelayLabel")
    currentClickerDelay.grid(row=0,column=4)

    delayClickEntryConfimButton = ttk.Button(root,text="Confirm",command=lambda t="clickButton": root.changeSpeeds(t,root.clickDelayEntry.get(),str(self.currentClickerDelay)))
    delayClickEntryConfimButton.grid(row=0,column=3)
        


def initJumperWidgets(root):
    jumpOnLabel = ttk.Label(root,text="Off",name="jumpLabel")
    jumpOnLabel.grid(row=1,column=1)

    jumpButton = ttk.Button(root,text="AutoJump",command=lambda t="jumpButton": root.changeButtonState(t,str(root.jumpOnLabel)))
    jumpButton.grid(row=1,column=0)

    jumpDelayEntry = ttk.Entry(root,width=5)
    jumpDelayEntry.grid(row=1,column=2)

    currentJumpDelay = ttk.Label(root,text="1",name="jumpDelayLabel")
    currentJumpDelay.grid(row=1,column=4)
    
    delayJumpEntryConfirmButton = ttk.Button(root,text="Confirm",command=lambda t="jumpButton": root.changeSpeeds(t,root.jumpDelayEntry.get(),str(self.currentJumpDelay)))
    delayJumpEntryConfirmButton.grid(row=1,column=3)
    
def initScanWidgets(root):
    scanOnLable = ttk.Label(root,text="Off",name="scanLabel")
    scanOnLable.grid(row=2,column=1)

    scanButton = ttk.Button(root,text="ScanClick",command=lambda t="scanButton": root.changeButtonState(t,str(root.scanOnLable)))
    scanButton.grid(row=2,column=0)

    numberOfRowsEntry = ttk.Entry(root,width=5)
    numberOfRowsEntry.grid(row=2,column=2)
    currentNumberOfRowsLabel = ttk.Label(root,text="4",name="numberOfRowsLabel")
    currentNumberOfRowsLabel.grid(row=2,column=4)

    moveCheck = IntVar()
    moveCheckBox = ttk.Checkbutton(root,text='Move', variable=moveCheck, onvalue=1,offvalue=0, command=lambda : root.changeMovement())
    moveCheckBox.grid(row=2,column=5)
    halfScreenCheck = IntVar()
    halfScreenScan = ttk.Checkbutton(root,text="Half Screen", variable=halfScreenCheck,onvalue=1,offvalue=0, command=lambda : root.changeScanWidth())
    halfScreenScan.grid(row=2,column=6)
    numberOfRowsConfirmButton = ttk.Button(root,text="Confirm",command=lambda t="scanButton": root.changeNumberOfRows(t,root.numberOfRowsEntry.get(),str(root.currentNumberOfRowsLabel)))
    numberOfRowsConfirmButton.grid(row=2,column=3)