import os
import platform
from colorama import Fore
from colorama import init
init()

class Commands:
    def Help():
        print("help - view all commands\texit - exit from program\tclear - clear all from terminal\nabout - description program\treadfile - read a file\tpython - open a python interpreter")
    def Clear():
        global system
        system = platform.system()
        if system == "Windows":
            os.system('cls')
        elif system == "Linux" or system == "Darwin":
            os.system('clear')
    def About():
        print("EyeTerminal - a console program, created just for fun.\nEyeTerminal has a open source code on github, and support platforms\n Windows\n Linux\n MacOS\n")
    def ReadFile(file):
        if os.path.exists(file):
            fileuser = open(file, 'r')
            print(fileuser.read())
        else:
            print(Fore.RED + "Error file doesn't exist" + Fore.RESET)
    def OpenPython():
        os.system('python')