import pyautogui
import pyscreeze #this import is needed for pyautogui even tho its not used
import time


#def reaction_time_module():
while True:
    if(pyautogui.pixelMatchesColor(300, 300,(75,219,106), tolerance=10)== True):
        pyautogui.click(x=300,y=300)
        time.sleep(0.5)