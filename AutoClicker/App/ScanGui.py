import threading
import pydirectinput
from win32api import GetSystemMetrics
import time as time

pydirectinput.PAUSE = 0.05
class ScanGui(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)               
        self.scanRunning = False
        self.program_running = True
        self.screenWidth = GetSystemMetrics(0)
        self.screenHeight = GetSystemMetrics(1)

        self.move = False
        self.totalNumberOfRows = 4   
        # amount if will go down on each row   
        self.heightOffSet = 10
        self.maxOffSet = 20

    def changeScanWidth(self,bool):
        if bool == True:
            newValue = int(self.screenWidth / 2)            
            self.screenWidth = newValue
        else:
            self.screenWidth = GetSystemMetrics(0)
          

    def changeMove(self,value):
        self.move = value
        print("move changed to ", self.move)

    def setNumberOfRows(self,value):
        try:
            self.totalNumberOfRows = float(value)               
            return True
        except ValueError:            
            return False 

    def isScanning(self):
        return self.scanRunning

    def startScanning(self):
        self.scanRunning = True

    def stopScanning(self):
        self.scanRunning = False

    def stop(self):
        self.program_running = False

    def scan(self):
        # goes to middle of screen plus a little
        newHeight = self.screenHeight *.5 + self.heightOffSet         
        nextLoopoffset = 0 
        numberOfLoops = 0        
        moveLoop = 0
        while nextLoopoffset < self.maxOffSet:       
            for x in range(150,self.screenWidth-250,10):
                if self.scanRunning == False:
                    break
                print(numberOfLoops)
                pydirectinput.moveTo(x,int(newHeight+nextLoopoffset))
                print("x = {}, y = {} offset = {}".format(x,int(newHeight-nextLoopoffset),nextLoopoffset))                      
                pydirectinput.click() 
            if self.scanRunning == False:
                break  
            
            
            nextLoopoffset += 5
            numberOfLoops += 1        
            if numberOfLoops > self.totalNumberOfRows: 
                nextLoopoffset = 0
                numberOfLoops = 0
                print("move = ", self.move)
                if self.move == True:
                    print("move is true should move")
                    print("move loop", moveLoop)
                    if moveLoop == 0:
                        pydirectinput.keyDown('a')
                        time.sleep(1)
                        pydirectinput.keyUp('a')
                        moveLoop = 1
                    else:
                        pydirectinput.keyDown('d')
                        time.sleep(1)
                        pydirectinput.keyUp('d')
                        moveLoop = 0

                

    def run(self):
        while self.program_running:            
            while self.scanRunning:
                self.scan()
            time.sleep(0.01)





        