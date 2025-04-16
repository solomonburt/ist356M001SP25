from datetime import datetime

def parsedate_mdy(text: str):
    return datetime.strptime(text, '%m/%d/%Y')

def formatdate_ymd(date: datetime):
    return date.strftime("%Y-%m-%d")

def test_parsedate_mdy():

def test_formatdate_ymd():

# write 2 asserts for each test function
