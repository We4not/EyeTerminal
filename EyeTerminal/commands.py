import os # importing for checking path
import platform # importing for get a name of system
import configparser # importing for config.cfg
import logging # importing for logging in log file
import msvcrt # importing for msvcrt.getch(), actually, is like in C# Method Console.ReadKey() but in python :D
import datetime # importing for get a date and log file
import socket # importing for connecting a server
from colorama import Fore
from colorama import init
init()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if os.path.exists("config.cfg") == False:
    print(Fore.RED + "Error! The file config.cfg doesn't exists" + Fore.RESET)
    msvcrt.getch()
    exit()

config = configparser.ConfigParser()
config.read("config.cfg")

recordlog = False
if config["DEBUG"]["LOG"] == "True": # checking a parameter in config.cfg
    if os.path.exists('log') == False: # if folder doesn't exists
        print(Fore.RED + "Error! The folder log doesn't exists" + Fore.RESET) # showing a error for user
        msvcrt.getch()
        exit()
    else: # if folder exists
        logging.basicConfig(level=logging.DEBUG, filename=datetime.datetime.now().strftime(r'log\\log_%H-%M-%S-%d-%m-%Y.log'), format="DATE: %(asctime)s %(levelname)s: %(message)s") # creating a log file and format
        recordlog = True # turn on a record log
class Commands:
    def Help(): # showing a list of commands
        print("\nhelp - view all commands\texit - exit from program\t\tclear - clear all from terminal\nabout - description program\treadfile - read a file\t\t\tpython - open a python interpreter\nls - show files in folder\tpip install - install a python module\tversion - show a version EyeTerminal\nlogtest - test a log\t\tconnect - connect in a server\n")
    def Clear(): # clear all from screen
        global system
        system = platform.system()
        if system == "Windows": # if system is windows then cls
            os.system('cls')
        elif system == "Linux" or system == "Darwin": # if system is linux or MacOS then clear
            os.system('clear')
    def About(): # description about EyeTerminal
        print("EyeTerminal - a console program, created just for fun.\nEyeTerminal has a open source code on github, and support platforms\n Windows\n Linux\n MacOS\n")
    def TestLog(): # writting in a log file
        if recordlog == True:
            logging.debug("A DEBUG Message")
            logging.info("An INFO")
            logging.warning("A WARNING")
            logging.error("An ERROR")
            logging.critical("A message of CRITICAL severity")
    def ReadFile(file): # reading a file, writted by user
        if os.path.exists(file):
            fileuser = open(file, 'r')
            print(fileuser.read()) # and show for user
            if recordlog == True:
                logging.info(fileuser.read())
        else:
            print(Fore.RED + "Error file doesn't exists" + Fore.RESET) # if EyeTerminal can't find a file, writted by user, then we show error for user
            if recordlog == True:
                logging.error("EyeTerminal: Error file doesn't exists")
    def OpenPython():
        os.system('python') # start a python interpreter
        if recordlog == True:
            logging.debug("EyeTerminal: calling a python.exe")
    def ShowAllFiles(): # showing all files in directory
        os.system('dir')
        if recordlog == True:
            logging.debug("EyeTerminal: calling a command >> dir")
    def InstallModulePip(modulename): # installing a module nammed by user
        os.system(f'pip install {modulename}') # install a module nammed by user
        if recordlog == True:
            logging.debug(f"EyeTerminal: calling a pip and argument install {modulename}")
    def Version(): # show a version
        print("EyeTerminal v1.1 beta")
        if recordlog == True:
            logging.info("EyeTerminal: EyeTerminal v1.1 beta")
    def Connect(address, port):
        print("WARNING! In server, log doesn't writting!")
        s.connect((address, port))
        s.sendall('Hello'.encode('utf-8'))
        data = s.recv(1024)
        s.close()
    def ShutDown(): # WARNING! Don't try call this function if you don't save a project, because he can really shutdown the computer (PC)
        if recordlog == True:
            logging.debug("EyeTerminal: calling a command >> shutdown /s /t 0")
            logging.debug("EyeTerminal: crashing a EyeTerminal...")
        os.system('shutdown /s /t 0') # shutting down the computer (PC)
        exit()