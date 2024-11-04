# Colors
from colorama import Fore, Back, Style

# Screen Clear
from clear import Clear

# Keyboard Input
from pynput import keyboard
from pynput.keyboard import Key, Listener

# Cursor hiding
import cursor
cursor.hide()

# Pages
from pages import Pages

sys_clear = Clear()

text = ""
cursor = Back.WHITE + " " + Style.RESET_ALL
modes = ['normal','inster','visual']
mode = "normal"
cmdinput = ""
pages = Pages()

# Screen Redraw
def redraw(action,extra):
    global mode
    global text
    global cursor
    global menu
    global cmdinput
    sys_clear.clear()
    
    # Mode Selection

    if (mode == "normal"):
        menu_mode = Fore.BLACK + Back.GREEN + "NORMAL" + Style.RESET_ALL
    if (mode == "insert"):
        menu_mode = Fore.WHITE + Back.RED + "INSERT" + Style.RESET_ALL   
    if (mode == "command"):
        #menu_mode = Fore.WHITE + Back.BLUE + "COMMAND" + Style.RESET_ALL   
        menu_mode = Fore.BLACK + Fore.CYAN + "COMMAND" + Style.RESET_ALL
 

    menu = menu_mode + " ViPy\n"


    if (action == "error"):
        print(menu_mode + " " + Fore.WHITE + Back.RED + "[ERROR] " + extra + Style.RESET_ALL + "\n")
        print(text+cursor)

    if (action == "entire"):
        if (extra == "startscreen"):
            print(menu)
            pageOutput = pages.startscreen()
            print(pageOutput)
        elif (extra == "help"):
            pageOutput = pages.helpscreen()
            print(pageOutput)
        else: 
            print(menu)
            print(text+cursor)

    if (action == "command"):
        if (extra == ""):
            cmdinput = cmdinput
        elif (extra == "backspace"):
            cmdinput = cmdinput[:-1]
        elif (extra == "space"):
            cmdinput = cmdinput + " "
        else:
            cmdinput = cmdinput + str(extra)[1]
        print(":"+ cmdinput + "\n") 
    
    if (action == "space"):
        print(menu)
        text = text + " ";
        print(text + cursor);

    if (action == "newline"):
        print(menu)
        text = text + "\n"
        print(text + cursor)

    if (action == "delete"):
        print(menu)
        text = text[:-1]
        print(text + cursor)

    if (action == "append"):
        print(menu)
        text = text + str(extra)[1]
        print(text + cursor);  

def on_press(key):
    global mode
    global cmdinput

    # Close the editor with alt key
    if (key == keyboard.Key.alt):
        sys_clear.clear()
        quit()
    if (key == keyboard.Key.esc):
        mode = "normal"
        cmdinput = ""
        redraw("entire","")

    # INSERT MODE
    if (mode == "insert"):
        if (key == keyboard.Key.backspace):
            redraw("delete","");
        elif (key == keyboard.Key.space):
            redraw("space","");
        elif (key == keyboard.Key.enter):
            redraw("newline","")
        else:
            try:
                redraw("append",key)
                #print('Key pressed: {0}'.format(key))
            except AttributeError:
                redraw("append",key)
                #print('Special key pressed {0}'.format(key))K
    # COMMAND MODE
    if (mode == "command"):
        if (key == keyboard.Key.backspace):
            redraw("command","backspace")
        elif (key == keyboard.Key.space):
            page_search()
        elif (key == keyboard.Key.enter):
            if (cmdinput == "quit") or (cmdinput == "q") or (cmdinput == "q!"):
                return False
            page_search()
        else:
            try:
                redraw("command",key)
                #print('Key pressed: {0}'.format(key))
            except AttributeError:
                redraw("command",key)
                #print('Special key pressed {0}'.format(key))K
    # NORMAL MODE
    if (mode == "normal"):
        if (hasattr(key,'char')):
            if (key.char == "i"):
                mode = "insert";
                redraw("entire","")
            elif (key.char == ":"):
                mode = "command"
                redraw("command","")
            else:
                redraw("error","there is no function for {0} in normal mode.".format(key))

def page_search():
    global mode
    global cmdinput
    mode = "normal"
    privateinput = cmdinput
    cmdinput = ""
    if (privateinput == "help"):
        redraw("entire","help")
    elif (privateinput == "q") or (privateinput == "q!") or (privateinput == "quit"):
        listener.stop()
        quit()

    elif (privateinput == "startscreen"):
        redraw("entire","startscreen")
    else:
        redraw("error","command '" + privateinput + "' does not exist.")

redraw("entire","startscreen")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join();
