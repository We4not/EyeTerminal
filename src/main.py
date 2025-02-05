import climage
import colorama
import sys
from sys import platform
from colorama import Fore
from scripts.user import User
from scripts.command import Command
from scripts.config import Config

colorama.init()

class EyeTerminal:
    def __init__(self):
        self.user = User()
        self.command = Command(self.user)

        self.config = Config()
        
        if self.config.GetPictureOnStart_Value():
            if platform == "win32" or platform == "linux2":
                self.output = climage.convert('../icon.png') # DON'T FORGET CHANGE PATH BEFORE BUILD APPLICATION!!!!

    def main(self):
        if self.config.GetPictureOnStart_Value():
            if platform == "win32" or platform == "linux2":
                print(self.output)

        print(f"{Fore.GREEN}Welcome to {self.config.GetTitle_Value()}{Fore.RESET}")

        while True:
            self.user.HandleWhile()
            self.command.HandleUserInput()


if __name__ == '__main__':
    EyeTerminal().main()
    sys.exit(0)