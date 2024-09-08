import os

class Package:
    def __init__(self):
        self.listofPackages = os.listdir("./package")
    def run(self, packagename):
        for package in self.listofPackages:
            if package == packagename:
                exec(open(f'./package/{package}/main.py').read())
    def updateListOfPackages(self):
        self.listofPackages = os.listdir("./package")
