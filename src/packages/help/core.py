import colorama
from colorama import Fore

colorama.init()

class Help:
    def __init__(self):
        self.name = "Help"
        self.version = "v1.1"

def main(args):
    if args != None:
        if args[0] == "-v":
            print(f"{Help().name} {Help().version}")
        else:
            print(f"{Fore.RED}Unknown argument!{Fore.RESET}")
    print("clear - clear from screen\n"
          "echo [TEXT] - prints the line\n"
          "exit - exit from program\n"
          "help [ARGS] - show this information\n"
          "     [ARGS]:\n"
          "\t\t-v - show version\n"
          "version - show current version\n")