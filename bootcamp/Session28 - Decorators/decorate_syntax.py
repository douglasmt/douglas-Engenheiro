def be_polite(fn):
    print("\n ---- \n")
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite # it makes que greet function to call be_polite
def greet():
    print("My name is Colt.")


@be_polite
def rage():
	print("I HATE YOU!")

# each one calls everything in wrapper and what is inside itself
greet() 
rage()