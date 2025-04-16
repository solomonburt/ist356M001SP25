# Challenge 1-4-1
from datetime import datetime

date = input("Enter date m/d/y")
now = datetime.strptime(date, '%m/%d/%Y')
nowstr = now.strftime("%Y-%m-%d")
print(nowstr)

def parsedate_mdy(date):
    now = datetime.strptime(date, '%m/%d/%Y')
    
    