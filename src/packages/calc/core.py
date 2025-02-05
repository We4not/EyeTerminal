import operator
import colorama
from colorama import Fore

colorama.init()

actions = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

def main(args):
    try:
        print(actions[args[1]](int(args[0]), int(args[2])))
    except Exception:
        print(f"{Fore.RED}Failed to calculate{Fore.RESET}")