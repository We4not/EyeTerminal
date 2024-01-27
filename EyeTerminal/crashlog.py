import logging
import os
import random
import datetime
import sys
randomtext = ["Who this reading lol", "What have you done?!", "This comment is unuseful lol", ":D",
              "Do you know?... ahh forget it, I forgot", "This problem is actually sucks", ":(",
              "Bruh", "Why are you reading this?", "Who this guy hold a crowbar? λ", "Bruh, how you get error crash? :P"]

class Error:
    list = ["Unknown error", "The file config.cfg or plugin.cfg doesn't exists", "Folder plugin or log doesn't exists",
            "Invalid plugin path currentplugin or sourcecodeplugin"]

#                   list of error
#       0 = Unknown error
#       20 = The file config.cfg or plugin.cfg doesn't exists
#       30 = Folder plugin or log doesn't exists
#       40 = invalid plugin path currentplugin or sourcecodeplugin 
#   
    error = int(sys.argv[1]) # sys.argv[1] get from first argument

if os.path.exists(r'log\\crash') == False: # if folder doesn't exists
    os.mkdir(r"log\\crash")
logging.basicConfig(level=logging.DEBUG, filename=datetime.datetime.now().strftime(r'log\\crash\\log-crash_%H-%M-%S-%d-%m-%Y.log'), format="DATE: %(asctime)s %(levelname)s: %(message)s") # creating a file log in log/crash, and setting up format
if Error.error == 0:
    Error.error = 0
elif Error.error == 20:
    Error.error = 20
elif Error.error == 30:
    Error.error = 30
elif Error.error == 40:
    Error.error = 40
else:
    Error.error = 0

logging.debug(randomtext[random.randint(0, 9)]) # this actually is unuseful code, so you can delete this code, because he generate a random text from array randomtext
logging.error(f"ERROR CODE {Error.error}")
if Error.error == 0:
    logging.info(f"Error {Error.error} = {Error.list[0]}")
elif Error.error == 20:
    logging.info(f"Error {Error.error} = {Error.list[1]}")
elif Error.error == 30:
    logging.info(f"Error {Error.error} = {Error.list[2]}")
elif Error.error == 40:
    logging.info(f"Error {Error.error} = {Error.list[3]}")