import colorama
import os
from scripts.config import Config
from scripts.user import User
from colorama import Fore

colorama.init()

def main(args):
    if args != None:
        if os.path.exists(args[0]):
            print(open(args[0], 'r').read())
        else:
            print(f"{Fore.RED + Config().GetTitle_Value()}: {Fore.RESET}cat: {Fore.RED}No such file or directory{Fore.RESET}")
    else:
        print("meow")