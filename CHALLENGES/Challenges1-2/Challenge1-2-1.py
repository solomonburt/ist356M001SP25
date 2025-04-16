# Code Challenge 1-2-1

for i in range(5):
    password = input("Enter the password: ")
    if password == "secret":
        print ("acess granted")
        break
    else:
        print ("invalid password")
else:
    print("You are locked out")