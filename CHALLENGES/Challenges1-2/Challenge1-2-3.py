# Code Challenge 1-2-3
color = ""
colors = []
while True:
    color = input("Enter a color: ")
    if color == "quit":
        break
    elif color not in colors:
        colors.append(color)
print(colors)
    
