import colorama
from pathlib import Path
from colorama import Fore

colorama.init()

class User:
    def __init__(self):
        self.input_text = None
        self.symbol = "$"
        self.working_dirPath = Path().resolve()
        self.error = {
            1 : 'No such file or directory'
        }
    
    # FIX ME
    '''
    def GoToDirPathDir(self, dirname):
        if os.path.exists(' '.join(dirname)) and os.path.isdir(' '.join(dirname)):
            self.working_dirPath = self.working_dirPath.joinpath(' '.join(dirname))
        else:
            print(Fore.RED + self.error[1] + Fore.RESET)
    

    def LevelDownPathDir(self):
        try:
            self.working_dirPath = Path(self.working_dirPath).parents[0]
        except IndexError:
            pass

    def GetWorkingPathDir(self):
        return self.working_dirPath
    '''

    def HandleWhile(self):
        self.input_text = input(f"{Fore.YELLOW}{self.working_dirPath}{Fore.RESET} {self.symbol} ")