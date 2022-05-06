#def ensure_correct_info(*args):
def ensure_correct_info(*args):
	# I want to pass any number of arguments to the function
	if "Colt" in args and "Steele" in args:
		# we use the args without star(*)
		return "Welcome back Colt!"
	return "Note sure who you are"

print(ensure_correct_info("hello", False, 78)) # Not sure who you are...

print(ensure_correct_info(1, True, "Steele", "Colt"))

