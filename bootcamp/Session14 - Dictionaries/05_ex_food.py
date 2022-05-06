# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
print(f"Food chosen {food} ")
'''
if food in bakery_stock.items():
    print(f"found {food} and {bakery_stock[food]} left")
else:
    print("We don't make that")
'''
# My answer
#if food in bakery_stock.keys():
#    print(str(bakery_stock[food]) + " left")
#else:
#    print("We don't make that")

quantity = bakery_stock.get(food) # using the list with get as filter, getting the value of the key
if quantity: # if the food randomly selected is in bakery_stock
    print("{} left".format(quantity)) # brings the value of the key to the print
else:
    print("we don't make that")