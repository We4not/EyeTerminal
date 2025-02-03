import climage
import sys
from sys import platform
from colorama import Fore
from scripts.user import User
from scripts.command import Command

class EyeTerminal:
    def __init__(self):
        self.user = User()
        self.command = Command()
        if platform == "linux" or platform == "linux2":
            self.output = climage.convert('../icon.png') # DON'T FORGET CHANGE PATH BEFORE BUILD APPLICATION!!!!

    def main(self):
        if platform == "linux" or platform == "linux2":
            print(self.output)

        print(Fore.GREEN + "Welcome to EyeTerminal!" + Fore.RESET)

        while True:
            self.user.HandleWhile()
            self.command.HandleUserInput(self.user.input_text)


if __name__ == '__main__':
    EyeTerminal().main()
    sys.exit(0)