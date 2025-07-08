import pyautogui
import pyscreeze
import time


screen_width, screen_height = pyautogui.size()

while True:
    if(pyautogui.pixelMatchesColor(300, 300,(75,219,106), tolerance=10)== True):
        pyautogui.click(x=300,y=300)
    