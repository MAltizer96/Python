from pynput.keyboard import Key, Controller
import threading
import time as time

class ButtonPush(threading.Thread):

    def __init__(self, keyString):
        threading.Thread.__init__(self)
        self.key = keyString
        self.active = False
        self.program_running = True  

    def setKey(self,key):
        self.key = key

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def stop(self):
        self.program_running = False

    def run(self): 
        while self.program_running:                          
            while self.active:     
                print(self.key)                                   
                self.keyboard.press(self.key) 
                self.keyboard.release(self.key) 
                time.sleep(self.delay)
            time.sleep(0.1) 
