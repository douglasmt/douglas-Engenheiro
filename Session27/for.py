# Custom For Loop

# for num in [1,2,3]
# for char in "hi there"

def my_for(iterable, func):
	iterator = iter(iterable) 
	# iterables turns into an iterable value
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			break
		else:
			func(thing)

# the func is run as the second parameter 
# on the first parameter
		
def square(x):
	print(x*x)

my_for("lol", print)
my_for([1,2,3,4,5], square)
