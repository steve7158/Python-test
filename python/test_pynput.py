from pynput.mouse import Button, Controller, Listener


def on_move(x,y):
    print('mouse is moved')

def on_click(x, y, button, pressed):
    print('mouse is clicked')

def on_scroll(x,y,dx,dy):
    print('mouse is scrolled')



with Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll
) as listener:
    listener.join()
