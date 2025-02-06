from datetime import datetime

'''
# Get all attributes of the datetime module
attributes = dir(datetime)
for attribute in attributes:
    print(attribute)

'''

text = input("Enter date m/d/y: ")
now = datetime.strptime(text, "%m/%d/%Y")
nowstr = now.strftime("%Y-%m-%d")
print(nowstr)







