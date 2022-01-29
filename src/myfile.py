import time
import datetime


class MyFile:
    def __init__(self,filename):
        self.file = open(filename, 'w')
    def write(self, data):
        self.file.writelines(str(data))
    def close(self):
        self.file.close()
