
class Controller:
    def __init__(self,view,model):
        self.view = view
        self.t_click = model[0]
        self.t_jump = model[1]
        self.t_hotKeys = model[2]
        

    def checkClickerState(self):
        if self.t_click.isClicking():
            return True
        return False
    
    def changeClickerState(self):        
        if self.t_click.is_alive():
            #print("current clicking state:{}",self.t_click.isClicking())
            if not self.t_click.isClicking():
                self.t_click.startClicking()
            else:
                self.t_click.stopClicking()
        # need to return an error

    def changeJumpState(self):
        if self.t_jump.is_alive():
            #print("ran")   
            if not self.t_jump.isJumping():
                self.t_jump.startJumping()
            else:
                self.t_jump.stopJumping()
                
    def changeThreadState(self, button):
        #print("button:{}",button)
        if button == "clickButton":
            self.changeClickerState()

        if button == "jumpButton":
            self.changeJumpState()            

    def changeDelaySpeed(self,button,value):
        thread = self.getThread(button)        
        thread.setDelay(value)

    def getThread(self,value):
        #print(value)
        if value == "clickButton":
            return self.t_click
        if value == "jumpButton":
            return self.t_jump
        return None

    def changeStateOff(self):
        self.t_click.stopClicking()
        self.t_jump.stopJumping()
        self.view.changeLabelStateOff()
