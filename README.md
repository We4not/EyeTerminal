# EyeTerminal
![icon](https://github.com/We4not/EyeTerminal/blob/main/icon.png?raw=true) <br>
EyeTerminal - a console program, created just for fun. <br>
EyeTerminal has support platforms: <br>
Windows  Linux  MacOS <br>
ATTENTION: <br>
  If you have a problem with EyeTerminal, please click issues and post your problem <br>

# How to use?
All commands: <br>
  `help` - view all commands <br>
  `exit` - exit from program <br>
  `clear` - clear all from terminal <br>
  `about` - show description about EyeTerminal <br>
  `readfile [file]` - reading a file and show all text in the file <br>
  `python [argument]` - openning a python interpreter with not arguments <br>
  `ls` - show files in folder (not finished) <br>
  `pip` [argument] - calling pip with argument <br>
  `connect` - connect in a server <br>
  `logtest` - writting test in log file <br>
  `version` - show a version EyeTerminal <br>
  `start [file]` - starting the file <br>
  `touch [namefile]` - create a file <br>
  `echo [text]` - print text in screen <br>
  `system` - get system name <br>
  `login` - get a login <br>
  `[packagename]` - run a package <br>
  
# How to build
Python isn't a compilible launguage, but you can build to executable file with pyinstaller<br>
To build, you need to write this command:
```
pyinstaller main.py --name EyeTerminal --icon icon.png
```
The `--name` argument is the name of the program <br>
The `--icon` argument is the program icon <br>

After this command, you should have a dist folder, in which the EyeTerminal folder is located, and finally our executable file:
- dist
  - EyeTerminal
    - EyeTerminal

But there is one problem, we cannot run the program because we are missing the package folder and the config.cfg file

Create a package folder and then create a config.cfg file in which we will write all the parameters:
```
[PROGRAM]
LOGIN = user

[DEBUG]
LOG = True
```
After this it should work