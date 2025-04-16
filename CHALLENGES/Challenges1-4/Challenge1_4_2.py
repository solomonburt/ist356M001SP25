# Challenge 1-4-2
from datetime import datetime



def parsedate_mdy(text: str):
    return datetime.strptime(text, '%m/%d/%Y')

def formatdate_ymd(date: datetime):
    return date.strftime("%Y-%m-%d")
    
# print(formatdate_ymd(parsedate_mdy(input("Enter date m/d/y"))))

text = input("Enter date m/d/y: ")
date = parsedate_mdy(text)
date_str = formatdate_ymd(date)
print(date_str)