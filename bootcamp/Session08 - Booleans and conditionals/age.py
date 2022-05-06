age = 65

# age >=2 and age =< 8 - child
# age <= 65 - senior

if not ((age >= 2 and age <= 8) or age >= 65):
	print("You are not a senior or a child")
else:
	print("You are teenager or adult")