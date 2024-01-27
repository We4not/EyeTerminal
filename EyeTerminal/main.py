from commands import * # importing a commands.py
from pluginmanager import * # importing a pluginmanager.py

print(config["PROGRAM"]["LOGIN"] + ", welcome to EyeTerminal")
if recordlog == True: # if record log is True
    logging.info(config["PROGRAM"]["LOGIN"] + ", welcome to EyeTerminal") # writting in log file
running = True
while running:
    user = input(" $ ")
    if recordlog == True: # if record log is True
        logging.info(config["PROGRAM"]["LOGIN"] + f": {user}") # writting in log file
    if user == "help":
        Commands.Help()
    elif user == "exit":
        if config["EXIT"]["QUESTION"] == "True": # if in config.cfg in sector [EXIT] and finally in QUESTION is True
            print("Press any key...")
            msvcrt.getch()
        running = False
    elif user == "clear":
        Commands.Clear()
    elif user == "about":
        Commands.About()
    elif user == "readfile":
        file = input("File: ")
        Commands.ReadFile(file)
    elif user == "python":
        Commands.OpenPython()
    elif user == "ls":
        Commands.ShowAllFiles()
    elif user == "pip install":
        modulename = input("ModuleName: ") # get a module name from input user
        Commands.InstallModulePip(modulename) # installing a module which user writted
    elif user == "version":
        Commands.Version()
    elif user == "shutdown":
        Commands.ShutDown() # WARNING! This function it can really shutdown the pc, don't try if you don't save project
    elif user == "logtest":
        Commands.TestLog()
    elif user == "connect":
        address = input("IP: ")
        port = int(input("PORT: "))
        Commands.Connect(address, port)
    else:
        print(Fore.RED + f"{user} Command not found." + Fore.RESET) # if user writted wrong command, then show this text in color red
        if recordlog == True: # if record log is True
            logging.error(f"EyeTerminal: {user} Command not found") # and writting in log file