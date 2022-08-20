import pyautogui
import threading
import time as time
pyautogui.FAILSAFE = True

class PushMouseButton(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)            
        self.clicking = False
        self.program_running = True
        self.delay = 1.0

    def isClicking(self):        
        return self.clicking


    def setDelay(self,value):
        try:
            self.delay = float(value)               
            return True
        except ValueError:            
            return False  

    def startClicking(self):
        time.sleep(3)
        self.clicking = True               

    def stopClicking(self):
        self.clicking = False        

    def stop(self):
        self.program_running = False

    def run(self): 
        while self.program_running:  
           # print("autoClicking program running")            
            while self.clicking:                                                    
                pyautogui.click()                    
                time.sleep(self.delay)
            time.sleep(0.1)