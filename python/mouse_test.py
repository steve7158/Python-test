from pynput.mouse import Button, Controller, Listener
mouse=Controller()
# pressed=Listner()

def on_move(x,y):
    print('Position {0}'.format((x,y)))
def on_click(x,y,button,pressed):
    print('{0} at {1}'.format('pressed' if pressed else 'Release', (x,y)))
    if not pressed:
        return False

def on_scroll(x,y,dx,dy):
    print('Scrolled {0}'.format((x,y)))

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
