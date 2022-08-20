import threading
from pynput import keyboard

class HotKeys(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.program_running = True
        self.controller = None
        self.listener = keyboard.Listener(on_press=self.onKeyPress)
        self.listener.start()
        #self.hotkey = keyboard.HotKey(keyboard.HotKey.parse('`'))              

    def setController(self,controller):
        self.controller = controller
        
    def onKeyPress(self,key): 
              
        #verify controller
        if self.controller != None:    
            #if the ` key is pressed        
            if key == keyboard.KeyCode(char='`'):     
                # tells controller to stop threads          
                self.controller.changeStateOff()   
                return True       


    def stop(self):
        print("stop ran")
        keyboard.Listener.stop
        self.program_running = False
       
    
    # def run(self):
    #     while self.program_running:  
    #         print("running")          
    #         with keyboard.Listener(on_press=self.onKeyPress) as listener:
    #             print("listening")                
    #             listener.join()