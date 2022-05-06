def print_square_of_7(): #This function does not return anything
	print(7**2)

print_square_of_7() # this will print the result of the function above

def square_of_7(): 
	print("I AM BEFORE THE RETURN!") # this will be printed
	return 7**2
	print("I AM AFTER THE RETURN!")

result = square_of_7()
print(result) # this will print the result of the second function 