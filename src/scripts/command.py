import sys

class Command:
    def __init__(self):
        self.command = {
            "exit" : sys.exit,
            "echo" : []
        }

    def HandleUserInput(self, user_input):
        if user_input in self.command:
            self.command[user_input]()