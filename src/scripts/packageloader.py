import os
import colorama
from importlib import import_module
from colorama import Fore

colorama.init()

class PackageLoader:
    def __init__(self, handle_command):
        self.command = handle_command
    
    def LoadPackages(self):
        for package in os.listdir("./packages/"):
            package_imported = import_module(f"packages.{package}.core")
            self.command.RegisterNewCommand(package, package_imported.main)
    
    # def LoadPackage(self, packagename, quiet=False):
    #     found = False
    #     for package in os.listdir("./packages/"):
    #         if packagename == package:
    #             package_imported = import_module(f"packages.{package}.core")
    #             self.command.RegisterNewCommand(package, package_imported.main)
    #             found = True
    #             break
    #     if quiet == False and found:
    #         print(f"{Fore.LIGHTGREEN_EX}Package found successfully{Fore.RESET}")