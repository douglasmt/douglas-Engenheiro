from random import random
# always must to be imported
def flip_coin(): # function creation
	if random() > 0.5: # if random gives more than 0.5 
		return "HEADS"
	else:
		return "TAILS"

print(flip_coin()) # it will call and return the return clause result


