import colorama
import os
from scripts.config import Config
from scripts.user import User
from colorama import Fore

colorama.init()

def main(args):
    if args != None:
        if os.path.exists(args[0]):
            for path in os.listdir(args[0]):
                print(path)
        else:
            print(f"{Fore.RED + Config().GetTitle_Value()}: {Fore.RESET}ls: {Fore.RED}No such file or directory{Fore.RESET}")
    else:
        for path in os.listdir(User().working_dirPath):
            print(path)