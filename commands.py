import os # importing for checking path
import platform # importing for get a name of system
import configparser # importing for config.cfg
import logging # importing for logging in log file
import datetime # importing for get a date and log file
import socket # importing for connecting a server
import psutil # get info about computer
from colorama import Fore
from colorama import init
from package import *
init() # colorama init

system = platform.system()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if os.path.exists("config.cfg") == False:
    print(Fore.RED + "Error! The file config.cfg doesn't exists" + Fore.RESET)
    exit()

config = configparser.ConfigParser()
config.read("config.cfg")

recordlog = False
if config["DEBUG"]["LOG"] == "True": # checking a parameter in config.cfg
    if os.path.exists('log') == False: # if folder doesn't exists
        print(Fore.RED + "Error! The folder log doesn't exists" + Fore.RESET) # showing a error for user
        exit()
    else: # if folder exists
        logging.basicConfig(level=logging.DEBUG, filename=datetime.datetime.now().strftime(r'log\\log_%H-%M-%S-%d-%m-%Y.log'), format="DATE: %(asctime)s %(levelname)s: %(message)s") # creating a log file and format
        recordlog = True # turn on a record log

class Commands:
    def Help(): # showing a list of commands
        print("\nhelp - view all commands\texit - exit from program\t\tclear - clear all from terminal\nabout - description program\treadfile <file> - read a file\t\tpython <argument> - open a python interpreter\nls - show files in folder\tpip <argument> - calling pip\t\tversion - show a version EyeTerminal\nlogtest - test a log\t\tconnect - connect in a server\t\tstart <file> - starting the program\nsystem - get system name\techo <text> - print text in screen\ttouch <namefile> - creating a file\nlogin - get a login\t\tchange-login <newlogin>\n")
    
    def Clear(): # clear all from screen
        os.system('cls' if os.name == 'nt' else 'clear') # cross-platform clear all from screen
    
    def About(): # description about EyeTerminal
        print("EyeTerminal - a console program, created just for fun.\nEyeTerminal has a open source code on github, and support platforms\n Windows\n Linux\n MacOS\n")
    
    def TestLog(): # writting in a log file
        if recordlog == True:
            logging.debug("A DEBUG Message")
            logging.info("An INFO")
            logging.warning("A WARNING")
            logging.error("An ERROR")
            logging.critical("A message of CRITICAL severity")
        elif recordlog == False:
            print(Fore.RED + "Error! Parameter LOG in config.cfg is " + config["DEBUG"]["LOG"] + Fore.RESET)
    
    def ReadFile(file): # reading a file, writted by user
        if os.path.exists(file):
            fileuser = open(file, 'r')
            print(fileuser.read()) # and show for user
            if recordlog == True:
                logging.info(fileuser.read())
        else:
            print(Fore.RED + "Error! File doesn't exists" + Fore.RESET) # if EyeTerminal can't find a file, writted by user, then we show error for user
            if recordlog == True:
                logging.error("Error! File doesn't exists")
    
    def Python(argument):
        os.system(f'python {argument}') # start a python interpreter if argument is not specified
        if recordlog == True:
            logging.debug(f"EyeTerminal: python {argument}")
    
    def CreateFile(file): # creating a file
        if os.path.exists(file) == True:
            getpermissionfromuser = input(Fore.YELLOW + "The file is already created" + Fore.RESET + "\nDo you want create again? y/n: ")
            if getpermissionfromuser == "Y" or getpermissionfromuser == "y":
                os.remove(file)
                open(file, 'x')
        else:
            open(file, 'x')
    
    def ChangeLogin(newlogin): # change old login to new
        config.set('PROGRAM', 'LOGIN', newlogin)
        if recordlog == True:
            logging.info(f"EyeTerminal: Changing old login to {newlogin}....")
        with open('config.cfg', 'w') as configfile:
            config.write(configfile)
    
    def GetLogin(): # get a login from config.cfg
        if recordlog == True:
            logging.info(config["PROGRAM"]["LOGIN"])
        print(config["PROGRAM"]["LOGIN"])
    
    def Delete(path, dir=False): # deleting a file or dir
        if dir == True:
            os.rmdir(path)
        else:
            os.remove(path)
    
    def GetSystem(): # get a name system
        if os.name == 'nt':
            picture = [ [Fore.LIGHTCYAN_EX + "                            .oodMMMM"],
                        ["                   .oodMMMMMMMMMMMMM"],
                        ["       ..oodMMM  MMMMMMMMMMMMMMMMMMM"],
                        [" oodMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"],
                        [" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"],
                        [" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"],
                        [" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"],
                        [" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"],
                        [" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"],
                        ["                                    "],
                        [" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"],
                        [" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"],
                        [" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"],
                        [" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"],
                        [" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM"],
                        [" `^^^^^^MMMMMMM  MMMMMMMMMMMMMMMMMMM"],
                        ["       ````^^^^  ^^MMMMMMMMMMMMMMMMM"],
                        ["                      ````^^^^^^MMMM"], ]
        if os.name == 'linux':
            picture = [ ["                          .88888888:."],
                        ["                         88888888.88888."],
                        ["                       .8888888888888888."],
                        ["                       888888888888888888"],
                        ["                       88' _`88'_  `88888"],
                        ["                       88 88 88 88  88888"],
                        ["                       88_88_::_88_:88888"],
                        ["                       88:::,::,:::::8888"],
                        ["                       88`:::::::::'`8888"],
                        ["                      .88  `::::'    8:88."],
                        ["                     8888            `8:888."],
                        ["                   .8888'             `888888."],
                        ["                  .8888:..  .::.  ...:'8888888:."],
                        ["                 .8888.'     :'     `'::`88:88888"],
                        ["                .8888        '         `.888:8888."],
                        ["               888:8         .           888:88888"],
                        ["             .888:88        .:           888:88888:"],
                        ["             8888888.       ::           88:888888"],
                        ["             `.::.888.      ::          .88888888"],
                        ["            .::::::.888.    ::         :::`8888'.:."],
                        ["           ::::::::::.888   '         .::::::::::::"],
                        ["           ::::::::::::.8    '      .:8::::::::::::."],
                        ["          .::::::::::::::.        .:888:::::::::::::"],
                        ["          :::::::::::::::88:.__..:88888:::::::::::'"],
                        ["           `'.:::::::::::88888888888.88:::::::::'"],
                        ["                  `':::_:' -- '' -'-' `':_::::'`"] ]
        if os.name == 'darwin':
            picture = [ [Fore.LIGHTGREEN_EX + "                                   .8"],
                        ["                                 .888"],
                        ["                               .8888'"],
                        ["                              .8888'"],
                        ["                              888'"],
                        ["                              8'"],
                        ["                 .88888888888. .88888888888."],
                        ["              .8888888888888888888888888888888."],
                        ["             .8888888888888888888888888888888888."],
                        ["            .&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'"],
                        [Fore.LIGHTYELLOW_EX + "            &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'"],
                        ["            &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'"],
                        ["            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:"],
                        [Fore.YELLOW + "            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:"],
                        ["            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:"],
                        ["            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%."],
                        [Fore.RED + "            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%."],
                        ["            `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%."],
                        ["             `00000000000000000000000000000000000'"],
                        [Fore.LIGHTMAGENTA_EX + "              `000000000000000000000000000000000'"],
                        ["               `0000000000000000000000000000000'"],
                        ["                 `###########################'"],
                        [Fore.CYAN + "                  `#######################'"],
                        ["                    `#########''########'"],
                        ["                      `\"\"\"\"\"\"'  `\"\"\"\"\"'"] ]
        for row in picture: # drawing a picture in screen
            print(' '.join(map(str, row)))
            if recordlog == True:
                logging.info(' '.join(map(str, row)))
        print(Fore.RESET + f"System: {system}\nCPU Name: {platform.processor()}\nCPU Cores: {psutil.cpu_count(logical=True)}\n")
        if recordlog == True:
            logging.info(f"System: {system}\nCPU Name: {platform.processor()}\nCPU Cores: {psutil.cpu_count(logical=True)}\n")
    
    def ShowAllFiles(): # showing all files in directory
        os.system('dir')
        if recordlog == True:
            logging.debug("EyeTerminal: calling a command >> dir")
    
    def Pip(argument):
        os.system(f'pip {argument}')
        if recordlog == True:
            logging.debug(f"EyeTerminal: pip {argument}")
    
    def Version(): # show a version
        print("EyeTerminal v1.3")
        if recordlog == True:
            logging.info("EyeTerminal: EyeTerminal v1.3")
    
    def Connect(address, port):
        print("WARNING! In server, log doesn't writting!")
        if recordlog == True:
            logging.warning("In server, log doesn't writting!")
        s.connect((address, port))
        s.sendall(input("message > "))
        data = s.recv(1024)
    
    def StartProgram(pathfile):
        os.system(f'{pathfile}')