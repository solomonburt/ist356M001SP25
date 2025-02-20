
#Q5
assert isinstance(area(1), float), "Test 1 failed"
assert area(0) == 0, "Test 2 failed"

#Q6
lyst = [1, 2, 3, 4, 5]
test = [x ** 2 for x in lyst]
print(test)


#Q7
email = "tomas.beuzen@fakemail.com"
domain = email.split('@')[-1].split(".com")[0]
print(domain)