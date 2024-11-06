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

text = "" # This is where the document text is stored
cursor = Back.WHITE + " " + Style.RESET_ALL # The cursor indicating where you are
modes = ['normal','instert','visual','command'] # All the modes. Not really used for much just here list them out
mode = "normal" # Set the Default Mode
cmdinput = "" # Command Mode Input Line
pages = Pages() # All pages are stored in this variable. See more in pages.py
version = ["0.2 alpha","11/04/24"]

# Screen Redraw (Used for everything)
def redraw(action,extra):
    global mode
    global text
    global cursor
    global menu
    global cmdinput
    global version
    sys_clear.clear()
    
    # Mode Selection
    # This is the little text in the top right
    if (mode == "normal"):
        menu_mode = Fore.BLACK + Back.GREEN + " NORMAL " + Style.RESET_ALL
    if (mode == "insert"):
        menu_mode = Fore.WHITE + Back.BLUE + " INSERT " + Style.RESET_ALL   
    if (mode == "command"):
        #menu_mode = Fore.WHITE + Back.BLUE + "COMMAND" + Style.RESET_ALL   
        menu_mode = ""
    if (mode == "visual"):
        menu_mode = Fore.WHITE + Back.RED + " VISUAL " + Style.RESET_ALL
    # Text to the right of the mode. Will eventually show file names
    menu = menu_mode + "\n"

    # Actions, being the first param, descirbe to function of the redraw. 
    # Extra, contains any other information that needs to be passed on, like error handling
    
    # Errors
    if (action == "error"):
        print(menu_mode + " " + Fore.WHITE + Back.RED + "[ERROR] " + extra + Style.RESET_ALL + "\n")
        print(text+cursor)
    if (action == "warn"):
        print(menu_mode + " " + Fore.WHITE + Back.YELLOW + "[WARN] " + extra + Style.RESET_ALL + "\n")
    # Shows pages or refreshes
    if (action == "entire"):
        if (extra == "startscreen"):
            print(menu)
            pageOutput = pages.startscreen()
            print(pageOutput)
        else:
            if (extra == "version"):
                print(menu_mode + Fore.LIGHTBLACK_EX + " Press any key to return to your document \n" + Style.RESET_ALL)   
                pageOutput = Fore.GREEN + "Version " + Style.RESET_ALL + version[0] + Fore.GREEN + "\nUpdated " + Style.RESET_ALL + version[1] 
                print(pageOutput)
            elif (extra == "help"):
                print(menu_mode + Fore.LIGHTBLACK_EX + " Press any key to return to your document \n" + Style.RESET_ALL)
                pageOutput = pages.helpscreen()
                print(pageOutput)
            else:
                print(menu)
                print(text+cursor)

    # Opens command mode
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
    
    # All of the following are used for insert mode
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
    # Return to normal mode if esc is pressed. Also clears command input.
    if (key == keyboard.Key.esc):
        mode = "normal"
        cmdinput = ""
        redraw("entire","")

    # INSERT MODE
    if (mode == "insert"):
        # Used for other keys that are not letters
        if (key == keyboard.Key.backspace):
            redraw("delete","");
        elif (key == keyboard.Key.space):
            redraw("space","");
        elif (key == keyboard.Key.enter):
            redraw("newline","")
        elif (key == keyboard.Key.shift) or (key == keyboard.Key.shift_l) or (key == keyboard.Key.shift_r):
            pass # Hacky fix. Pressing shift prints 'e' for some reason.
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
        elif (key == keyboard.Key.shift) or (key == keyboard.Key.shift_l) or (key == keyboard.Key.shift_r):
            pass
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
        # Keybinds for switching into different modes
        if (hasattr(key,'char')):
            if (key.char == "i"):
                mode = "insert";
                redraw("entire","")
            elif (key.char == "v"):
                mode = "visual"
                redraw("entire","")
            elif (key.char == ":"):
                mode = "command"
                redraw("command","")
            else:
                redraw("error","there is no function for {0} in normal mode.".format(key))
    if (mode == "visual"):
        redraw("warn","visual mode has not been implemented yet.")
# Command Mode Runner. Its called page_search because it was originally intended to open pages but other commands are passed through aswell.
def page_search():
    global mode
    global cmdinput
    # Changes back to normal mode, clears cmdinput, and moves it into privateinput when addressing it later.
    mode = "normal"
    privateinput = cmdinput
    cmdinput = ""
    # Help
    if (privateinput == "help"):
        redraw("entire","help")
    # Quit
    elif (privateinput == "q") or (privateinput == "q!") or (privateinput == "quit"):
        listener.stop()
        quit()
    # Startscreen 
    elif (privateinput == "startscreen"):
        redraw("entire","startscreen")
    elif (privateinput == "version"):
        redraw("entire","version")
    # Error
    else:
        redraw("error","command '" + privateinput + "' does not exist.")




# Show start screen
redraw("entire","startscreen")


# Start the listener
# surpress=true is a hacky way of preventing typing inside the terminal while in the editor. 
# this is not a great way of doing things as it prevents multitasking but whatever.
with keyboard.Listener(suppress=True,on_press=on_press) as listener:
    listener.join();
