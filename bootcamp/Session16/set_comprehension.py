# tuples , ordered
# set  - no add or remove
# for a range 0 to 9, create a set
print(list(range(10)))
print("List is always ordered : ")
print([x**2 for x in range(10)])
# set - no order, add and remove
set_c = {x**2 for x in range(10)}
print(type(set_c))
print("No order when it is a set:")
print(set_c)