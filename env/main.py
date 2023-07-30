'''
                                                    Double Click Macro

    This is the main file of the script, the one that will detect the keys and button inputs and execute the basic actions.

    Author: Zourethe
    Date: July, 16, 2023
'''

# Libraries imports.
from pynput import mouse, keyboard
from time import sleep

# Variables definition.
mouseC = mouse.Controller()
countL = 0
countR = 0
toggle = False

# On click function definition.
def on_click(x, y, button, pressed):
    global countL, countR, toggle
    if button == mouse.Button.button9:
        if toggle == False:
            toggle = True
            print('Toggled')
        else:
            toggle = False
            print('Untoggled')
    if button == mouse.Button.left and pressed and toggle:
        countL = countL + 1
        if countL == 2:
            countL = 0
            sleep(0.12)
            mouseC.press(mouse.Button.left)
            sleep(0.001)
            mouseC.release(mouse.Button.left)
    elif button == mouse.Button.right and pressed and toggle:
        countR = countR + 1
        if countR == 2:
            countR = 0
            sleep(0.12)
            mouseC.press(mouse.Button.right)
            sleep(0.001)
            mouseC.release(mouse.Button.right)

# Pynput listeners definition.
ms_lstnr = mouse.Listener(on_click = on_click)

# Pynput listeners start.
ms_lstnr.start()
ms_lstnr.join()
