from pynput.keyboard import Key, Controller
import threading
import time as time
import random

class PushButtons(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)        
        self.keyboard = Controller() 
        self.jumping = False
        self.program_running = True
        self.delay = 1
        
    def startJumping(self):
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
                self.keyboard.press(Key.space) 
                self.keyboard.release(Key.space) 
                time.sleep(self.delay)
            time.sleep(0.1)
        