'''
                                                    Double Click Macro

    This is the main file of the script, the one that will detect the keybind and execute the actions.

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

# Terminal interface.
print("\033[32m{}\033[0m".format("                  Double Click Macro"))
print("")
print("\033[0m{}\033[0m".format("This is a double click macro script, to use it\njust hold the \033[31mMouse5\033[0m button and click. It works\nfor both left and right click."))
print("")
print("\033[0m{}\033[0m".format("Script by Zourethe."))
print("")

# On click function definition.
def on_click(x, y, button, pressed):
    global countL, countR, toggle
    if button == mouse.Button.button9:
        if toggle == False:
            toggle = True
            print("\033[32m{}\033[0m".format("Macro toggled"))
        else:
            toggle = False
            print("\033[31m{}\033[0m".format("Macro untoggled"))
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
