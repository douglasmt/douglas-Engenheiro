def offer():
	return "Hey do you like apples?"

def bake():
	return "Mmmm, pie..."

def hi():
	print(f"Printing {__name__}")

offer()

if __name__ == "__main__":
	hi() 
	# if apples is imported will print Printing apples