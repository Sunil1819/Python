import os
import datetime
class File:
    def __init__(self,d):
        self.d=d
    def getmaxsizeFile(self,count):
        files = [(f, os.path.getsize(os.path.join(self.d, f))) for f in os.listdir(self.d) if os.path.isfile(os.path.join(self.d,f))]
        files.sort(key=lambda x: x[1], reverse=True)
        return [file[0] for file in files[:count]]
    def getlatestFiles(self,date):
        files = [(f, os.path.getmtime(os.path.join(self.d, f))) for f in os.listdir(self.d) if os.path.isfile(os.path.join(self.d,f))]
        filtered_files = [file[0] for file in files if datetime.datetime.fromtimestamp(file[1]).date()>date]
        return filtered_files