import os


class createDir:
    
    def __init__(self, path):
        self.make(path)
        

    def make(self, path):
        if not os.path.exists(path):
            os.makedirs(path)