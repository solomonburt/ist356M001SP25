# Code Challenge 1-2-4
# Write a program to create a shopping list
# loop until "quit" is entered. input a grocery item input a quantity
# save the item as the key in the dictionary and wuantity as the value
# if the item is intthe dictionary already, add the wuantity to the
# existing value

groceryList = {}
while True:
    grocery = input("Enter an item from the grocery store (type 'quit' to exit): ")
    if grocery == "quit":
        break
    else:
        amount = int(input("How many of that item?: "))
        if grocery not in groceryList:
            groceryList[grocery] = amount
        else:
            groceryList[grocery] = groceryList[grocery] + amount
print("Your grocery list: ",groceryList)