# A User class with 3 attributes but no methods (aside from __init__)
class User:
	def __init__(prop_User, first, last, age): # every class has __init__ method
		# self - specific instance of object - I changed to prop_User
		#  it must always be the first parameter
		# * every object has different values for first,last and age
		prop_User.first = first
		prop_User.last = last
		prop_User.age = age
		print("\nUser created!\n")

# * every object has different values for first,last and age
user1 = User("Joe","Smith", 68)
user2 = User("Blanca", "Lopez", 41)
# two instances of the User class created

print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)






