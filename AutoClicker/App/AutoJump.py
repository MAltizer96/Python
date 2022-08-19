import pyautogui
import threading
import time as time
pyautogui.FAILSAFE = True
class PushButtons(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)    
       
        self.jumping = False
        self.program_running = True
        self.delay = 1.0
    
    def isJumping(self):
        return self.jumping

    def setDelay(self,value):
        try:
            self.delay = float(value)               
            return True
        except ValueError:
            print("cant use that number")
            return False 

    def startJumping(self):
        time.sleep(3)
        self.jumping = True 
        print("Started Jumping")
        
 
        
    def stopJumping(self):
        self.jumping = False 
        print("Stopped Jumping")
        
    def stop(self):
        self.program_running = False       
        
    def run(self):        
        while self.program_running:
            #print("AutoJump program running")               
            while self.jumping:     
                print("Jump")                                   
                pyautogui.press('space')                
                time.sleep(self.delay)
            time.sleep(0.1)
        