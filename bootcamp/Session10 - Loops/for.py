# for x in range(1,10):
# 	print(x)
# 	print(x*x)

def print_loop(operators):
	if operators == "string":
		for letter in "coffee": # prints each letter
			print(letter*10)
	elif operators == "range1":
		for number in range(1,9): # prints each number from 1 to 8(without 9)
			print(number)
	elif operators == "range9":
		for number in range(9): # prints each number from 0 to 8(9 numbers without 9)
			print(number)
	elif operators == "odds":
		for number in range(1,10,2): # prints odds without 20
			print(number)
	elif operators == "int7to1":
		for number in range(7,0,-1): # integers from 7 to 1
			print(number)
	elif operators == "q4":
		for number in range(8,0,-2): # integers from 7 to 1
			print(number)

print_loop("q4")

