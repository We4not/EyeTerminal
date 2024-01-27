from commands import *
from colorama import Fore # importing for color text
from colorama import init # importing for color text
init() # initialitize a colorama
from pluginmanager import * # importing a pluginmanager.py
import msvcrt # for a msvcrt.getch(), actually, it's like in C# Console.ReadKey();
import configparser # importing for config
import logging # importing for log file
import datetime # importing for get a date for log file
import os # importing for a checker path exists

config = configparser.ConfigParser()
config.read("config.cfg")
if config["PROGRAM"]["DEVELOPEMENTMODE"] == "True": # checking a parameter in file config.cfg
    devmode = True
elif config["DEBUG"]["LOG"] == "True":
    if os.path.exists('log') == False: # if folder doesn't exists
        print(Fore.RED + "Error! The folder log doesn't exists, please create a folder with name log" + Fore.RESET)
        msvcrt.getch()
        exit()
    else: # if folder exists
        logging.basicConfig(level=logging.INFO, filename=datetime.datetime.now().strftime(r'log\\log_%H-%M-%S-%d-%m-%Y.log'), format="%(asctime)s %(levelname)s %(message)s")
        recordlog = True

print(config["PROGRAM"]["LOGIN"] + ", welcome to EyeTerminal")

running = True
while running:
    user = input(" $ ")
    if user == "help":
        Commands.Help()
    elif recordlog == True:
        logging.info(user)
    if user == "exit":
        if config["EXIT"]["QUESTION"] == "True":
            print("Press any key...")
            msvcrt.getch()
        running = False
    elif user == "clear":
        Commands.Clear()
    if user == "about":
        Commands.About()
    elif user == "readfile":
        file = input("File: ")
        Commands.ReadFile(file)
    if user == "python":
        Commands.OpenPython()
    elif user == "ls":
        Commands.ShowAllFiles()
    if user == "pip install":
        modulename = input("ModuleName: ")
        Commands.InstallModulePip(modulename)
    elif user == "version":
        Commands.Version()
    if user == "shutdown":
        Commands.ShutDown()
    else:
        print(Fore.RED + f"{user} Command not found." + Fore.RESET)
exit()