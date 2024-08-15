from commands import * # importing a commands.py

print(config["PROGRAM"]["LOGIN"] + ", welcome to EyeTerminal")
if recordlog == True: # if record log is True
    logging.info(config["PROGRAM"]["LOGIN"] + ", welcome to EyeTerminal") # writting in log file
running = True
while running:
    user = input(" $ ")
    if recordlog == True: # if record log is True
        logging.info(config["PROGRAM"]["LOGIN"] + f": {user}") # writting in log file
    if user == "help": # show all commands
        Commands.Help()
    elif user == "exit":
        running = False
    elif user == "clear": # clear all from screen
        Commands.Clear()
    elif user == "about": # description about EyeTerminal
        Commands.About()
    elif user[0:8] == "readfile": # reading a file, readfile <argument>
        if len(user) <= 8:
            print(Fore.RED + "Error! Argument <file> is not specified" + Fore.RESET)
            if recordlog == True:
                logging.error("Error! Argument <file> is not specified")
        else:
            Commands.ReadFile(user[9:len(user)])
    elif user[0:6] == "python":
        Commands.Python(user[6:len(user)])
    elif user == "ls": # show all files in directory
        Commands.ShowAllFiles()
    elif user[0:3] == "pip": # calling a pip with argument if specified, if not specified, then we just calling pip with not arguments
        Commands.Pip(user[4:len(user)])    
    elif user == "version":
        Commands.Version()
    elif user == "system":
        Commands.GetSystem()
    elif user[0:12] == "change-login":
        if len(user) <= 13:
            print(Fore.RED + "Error! Argument <newlogin> is not specified" + Fore.RESET)
            if recordlog == True:
                logging.error("Error! Argument <newlogin> is not specified")
        else:
            Commands.ChangeLogin(user[13:len(user)])
    elif user == "login":
        Commands.GetLogin()
    elif user[0:4] == "echo":
        print(user[5:len(user)])
    elif user[0:5] == "touch":
        if len(user) <= 6:
            print(Fore.RED + "Error! Argument <file> is not specified" + Fore.RESET)
            if recordlog == True:
                logging.error("Error! Argument <file> is not specified")
        else:
            Commands.CreateFile(user[6:len(user)])
    elif user == "shutdown":
        Commands.ShutDown() # WARNING! This function it can really shutdown the pc, don't try if you don't save project
    elif user == "logtest":
        Commands.TestLog()
    elif user == "connect": # connecting in server
        address = input("IP: ") # get ip from input
        port = int(input("PORT: ")) # get port from input
        Commands.Connect(address, port) # connect to server
    elif user[0:5] == "start":
        if len(user) <= 6:
            print(Fore.RED + "Error! Argument <pathfile> is not specified" + Fore.RESET)
            if recordlog == True:
                logging.error("Error! Argument <pathfile> is not specified")
        else:
            Commands.StartProgram(user[6:len(user)])
    else:
        print(Fore.RED + f"{user} Command not found." + Fore.RESET) # if user writted wrong command, then show this text in color red
        if recordlog == True: # if record log is True
            logging.error(f"{user} Command not found") # and writting in log file