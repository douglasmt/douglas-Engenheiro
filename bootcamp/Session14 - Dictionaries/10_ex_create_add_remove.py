inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = dict(inventory)


# add the value 18 to stock_list under the key "cookie"
new_key = {"cookie": 18}
stock_list.update(new_key)

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop("cake")

print(stock_list)