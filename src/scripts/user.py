import os
from pathlib import Path
from colorama import Fore

class User:
    def __init__(self):
        self.input_text = None
        self.symbol = " $ "
        self.working_dirPath = Path().resolve()
        self.error = {
            1 : 'No such file or directory'
        }
    
    def GoToDirPathDir(self, dirname):
        if os.path.exists(f"{self.working_dirPath}/{dirname}") and os.path.isdir(f"{self.working_dirPath}/{dirname}"):
            self.working_dirPath = self.working_dirPath.joinpath(f"{dirname}")
        else:
            print(Fore.RED + self.error[1] + Fore.RESET)

    def LevelDownPathDir(self):
        try:
            self.working_dirPath = Path(self.working_dirPath).parents[0]
        except IndexError:
            pass

    def GetWorkingPathDir(self):
        return self.working_dirPath
    
    def HandleWhile(self):
        self.input_text = input(str(self.working_dirPath) + self.symbol)