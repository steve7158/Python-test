import pyautogui as pa
from graphics import *
from pynput import mouse

win=GraphWin('test', 1388, 768)
def painter():
    while(True):
    
        x,y=pa.position()
        pt=Point(x,y)
        pt.draw(win)
