import configparser
import os
from commands import *
plugin = configparser.ConfigParser()
if os.path.exists("plugin.cfg") == False:
    print(Fore.RED + "Error! The file plugin.cfg doesn't exists" + Fore.RESET)
    msvcrt.getch()
    exit()
plugin.read("plugin.cfg")
loadplugin = True
if plugin["PLUGINS"]["currentplugin"] == "None" and plugin["PLUGINS"]["sourcecodeplugin"] == "None":
    loadplugin = False
elif loadplugin == True:
    if os.path.exists(str(plugin["PLUGINS"]["currentplugin"])):
        print(Fore.LIGHTGREEN_EX + plugin["PLUGINS"]["currentplugin"] + Fore.RESET)
        folderexist = True
    else:
        error = True
        print(Fore.RED + "Error! The folder doesn't exists." + Fore.RESET)
        os.system('pause')
        exit()
    if os.path.exists(str(plugin["PLUGINS"]["sourcecodeplugin"])):
        print(Fore.LIGHTGREEN_EX + plugin["PLUGINS"]["sourcecodeplugin"] + Fore.RESET)
        sourcecodeexist = True
    else:
        error = True
        print(Fore.RED + "Error! The source code plugin doesn't exists." + Fore.RESET)
        os.system('pause')
        exit()

    if folderexist == True and sourcecodeexist == True:
        print(Fore.LIGHTGREEN_EX + "Plugin has been loaded!" + Fore.RESET)