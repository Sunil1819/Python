from DAY4F1Q1 import File
import datetime
fs=File(".")
print(fs.getmaxsizeFile(2)) 
print(fs.getlatestFiles(datetime.date(2018,2,1)))
