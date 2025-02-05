import configparser

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("./cfg/config.cfg")
    
    def GetTitle_Value(self):
        return self.config['main']['title']
    
    def GetVersion_Value(self):
        return self.config['main']['version']
    
    def GetPictureOnStart_Value(self):
        return True if self.config['advanced']['pictureonstart'] == "true" else False