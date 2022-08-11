from pynput.mouse import Button, Controller
import threading
import time as time
import random

class PushMouseButton(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)        
            self.mouse = Controller() 
            self.clicking = False
            self.program_running = True
            self.delay = 1

        def startClicking(self):
            self.clicking = True
            print("Started Clicking")

        def stopClicking(self):
            self.clicking = False
            print("Stopped Clicking")

        def stop(self):
            self.program_running = False

        def run(self): 
            while self.program_running:  
                #print("autoClicking program running")            
                while self.clicking:    
                    print("click")                     
                    time.sleep(1)                   
                    self.mouse.press(Button.left)
                    time.sleep(.5)
                    self.mouse.release(Button.left) 
                    time.sleep(self.delay)
                time.sleep(0.1)