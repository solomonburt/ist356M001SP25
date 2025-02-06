from datetime import datetime

def parsedate_mdy(text: str):
    """
    Parses a date in the format mm/dd/yyyy and returns a datetime object.
    """
    return datetime.strptime(text, '%m/%d/%Y')

def formatdate_ymd(date: datetime):
    """
    Takes a datetime object and returns a string in the format yyyy-mm-dd.
    """
    return date.strftime("%Y-%m-%d")

# Calling the functions
text = input('Enter date m/d/y: ')
date = parsedate_mdy(text)
date_str = formatdate_ymd(date)
print(date_str)
