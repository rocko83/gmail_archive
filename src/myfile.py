import time
import datetime
import logging

class MyFile:
    def __init__(self,filename):
        self.filename = filename
        self.file = open(filename, 'w')
        logging.debug(f"Open_file {self.filename}")
    def write(self, data):
        self.file.writelines(str(data))
        logging.debug(f"Archived_file {self.filename}")
    def close(self):
        self.file.close()
        logging.debug(f"File_close {self.filename}")
