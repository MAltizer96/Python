from pynput.mouse import Button, Controller
import pydirectinput
import time
from win32api import GetSystemMetrics
pydirectinput.FAILSAFE = True

def main():             
    # for x in range(0)
    # pyautogui.moveTo
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)    
    time.sleep(1)
     
    for y in range(150,height-250,10):
        for x in range(150,width-250,10):
            pydirectinput.moveTo(x,y)
            print("x = {}, y = {}".format(x,y))  
            #dwtime.sleep(.01)           
            pydirectinput.click()       
            


if __name__ == "__main__":
    main()