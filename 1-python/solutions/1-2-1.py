# Challenge 1-2-1

valid_pw = "secret"

for i in range(5):
    pw = input("Enter your password: ")
    if pw == valid_pw:
        print("Access granted")
        break
    else:
        print("Invalid password")
else:
    print("You are locked out")

