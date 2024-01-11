from commands import *
from colorama import Fore
from colorama import init
init()

picture = [ ["⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄"],
            ["⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⡀⠄⠄⢀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄"],
            ["⠄⠄⠄⠄⣠⣄⠄⠄⠈⣿⡇⠄⠄⢸⣿⠁⠄⠄⣠⣄⠄⠄⠄⠄"],
            ["⠄⠄⠄⠄⠙⣿⣆⠄⠄⢻⣿⠄⠄⣿⡟⠄⠄⣰⣿⠋⠄⠄⠄⠄"],
            ["⠻⣷⣄⠄⠄⠙⠟⠄⢀⣀⣁⣠⣄⣈⣀⡀⠄⠻⠋⠄⠄⣠⣾⠟"],
            ["⠄⠈⠻⠷⠄⣠⣴⠾⠟⠛⢻⣿⣿⣿⣿⡿⠷⣦⣄⠄⠾⠟⠁⠄"],
            ["⠄⠄⢀⣴⡾⠛⠁⠄⣤⣤⣾⣿⣿⣿⣿⣿⠄⠈⠛⢷⣦⡀⠄⠄"],
            ["⠄⠄⢾⣯⡀⠄⠄⠄⠻⣿⣿⣿⣿⣿⣿⠟⠄⠄⠄⢀⣽⡷⠄⠄"],
            ["⠄⠄⠄⠙⢿⣦⡀⠄⠄⠈⠻⠿⠿⠟⠁⠄⠄⢀⣴⡿⠋⠄⠄⠄"],
            ["⠄⠄⠄⠄⠄⠈⠛⠷⣶⣤⣤⣀⣀⣤⣤⣶⠾⠛⠁⠄⠄⠄⠄⠄"],
            ["⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠉⠉⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄"],
            ["⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄"],
            ["⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄"], ]

for i in range(len(picture)):
    for j in range(len(picture[i])):
        print(Fore.GREEN + picture[i][j], end=' ')
    print()

print(Fore.RESET + "Welcome to EyeTerminal")

running = True
while running:
    user = input(" $ ")
    if user == "help":
        Commands.Help()
    elif user == "exit":
        running = False
    elif user == "clear":
        Commands.Clear()
    elif user == "about":
        Commands.About()
    else:
        print(f"{user} Command not found.")

exit()