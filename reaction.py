import pyautogui
import pyscreeze #this import is needed for pyautogui even tho its not used
import time


def start_reaction_module(R,G,B,posx,posy):
    while running:
        if(pyautogui.pixelMatchesColor(posx, posy,(R,G,B), tolerance=10)== True):
            pyautogui.click(x=posx,y=posy)