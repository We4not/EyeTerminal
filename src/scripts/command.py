import os
import sys
import colorama
from colorama import Fore
from scripts.user import User
from scripts.packageloader import PackageLoader
from scripts.config import Config

colorama.init()

class Command:
    def __init__(self, user : User):
        self.user = user
        self.config = Config()
        
        self.command = {
        #   Command       Function
            #"cd" : self.user.GoToDirPathDir,
            "clear" : self.__clear_console,
            "exit" : sys.exit,
            "echo" : self.__echo_command,
            "version" : self.__version_command
            #"ls" : self.__ls_command
        }

        self.packageloader = PackageLoader(self)
        self.packageloader.LoadPackages()

        # for package in os.listdir("./packages/"):
        #     package_imported = import_module(f"packages.{package}.core")
        #     self.RegisterNewCommand(package, package_imported.main)

    def __clear_console(self, args):
        os.system('cls' if sys.platform == 'win32' else 'clear')
    
    def __echo_command(self, args):
        print(' '.join(args))
    
    def __version_command(self, args):
        print(self.config.GetTitle_Value(), self.config.GetVersion_Value())

    def RegisterNewCommand(self, text, command_func):
        self.command[text] = command_func

    # def __ls_command(self, args):
    #     print(os.listdir(self.user.GetWorkingPathDir()))


    def HandleUserInput(self):
        args = self.user.input_text.split()
        if args[0] in self.command:
            if len(args) > 1:
                self.command[args[0]](args[1:None])
            else:
                self.command[args[0]](None)
        else:
            print(f"{Fore.RED}{self.config.GetTitle_Value()}: {Fore.RESET}{args[0]}{Fore.RED}: command not found{Fore.RESET}")