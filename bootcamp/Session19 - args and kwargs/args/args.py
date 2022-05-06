def feed_me(*stuff):
	for thing in stuff:
		print(f"YUMMY I EAT {thing}")
feed_me("apple", "tire", "shoe", "salmon")


feed_var = ("apple", "tire", "shoe", "salmon")
feed_me(*feed_var) # as a variable with a list inside it will just accept *feed_var