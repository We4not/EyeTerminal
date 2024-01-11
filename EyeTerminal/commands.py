import os
import platform

class Commands:
    def Help():
        print("help - view all commands\texit - exit from program\tclear - clear all from terminal")
    def Clear():
        system = platform.system()
        if system == "Windows":
            os.system('cls')
        elif system == "Linux" or system == "Darwin":
            os.system('clear')

    def About():
        print("EyeTerminal - a console program, created just for fun.\nEyeTerminal has a open source code on github, and support platforms\n Windows\n Linux\n MacOS\n")