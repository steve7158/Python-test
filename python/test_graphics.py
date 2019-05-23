from graphics import *
import pyautogui as pa
from pynput import mouse
def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def clear(win):
    for items in win.items[:]:
        item.undraw()
    win.update()

win=GraphWin('test',1388,768)
while(True):
    (x,y)=pa.position()

    pt=Point(x,y)
    pt.draw(win)

with Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
