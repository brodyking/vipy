from colorama import Fore, Back, Style
class Pages:
    def startscreen(self):
        line0="       __   __   __     ______   __  __    \n"
        line1="      /\ \ / /  /\ \   /\  == \ /\ \_\ \   \n"
        line2="      \ \ \'/   \ \ \   \ \  _-/ \ \____ \  \n"
        line3="       \ \__|    \ \_\  \ \_\    \/\_____\ \n"
        line4="        \/_/      \/_/   \/_/     \/_____/ \n\n"
        line5="             ViPy (c) 2024 Brody King        \n\n"
        line6="     To get started, press : and type help.  \n"
        return Fore.LIGHTBLACK_EX +line0+line1+line2+line3+line4+line5+line6+Style.RESET_ALL



    def helpscreen(self):
        fl = Fore.LIGHTGREEN_EX
        sl = Fore.GREEN
        tl = Fore.WHITE
        ol = Fore.BLUE
        line = []
        line.append(fl+"Help")
        line.append(sl+"    > About")
        line.append(tl+"        > ViPy is a vim-ish text editor.")
        line.append(tl+"        > not much more to know")
        line.append(fl+"")
        line.append(sl+"    > Commands")
        line.append(tl+"        > :help")
        line.append(ol+"            > displays basic commands and functions")
        line.append(tl+"        > :quit")
        line.append(ol+"            > quits app. ")
        line.append(ol+"            > alias: !q and alt.")
        line.append(tl+"        > :startscreen")
        line.append(ol+"            > shows the logo and starting information")
        line.append(tl+"        > :version")
        line.append(ol+"            > shows the current version")
        output = ""
        i = 0;
        while (i<len(line)):
            output += line[i] + "\n"
            i += 1
        return output + Style.RESET_ALL