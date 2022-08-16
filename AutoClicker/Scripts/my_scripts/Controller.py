from ButtonPush import ButtonPush
class Controller:
    def __init__(self,view):

        self.view = view
        self.currentButtons = {}

    def activateButton(self,buttonBool,buttonName):
        if buttonBool:
            if buttonName not in self.currentButtons:
                self.currentButtons[buttonName] = ButtonPush(buttonName)
                self.currentButtons[buttonName].activate()
                return
            self.currentButtons[buttonName].activate()
            return
        self.currentButtons[buttonName].deactivate()
        
        

                    
                        