x = 0
y = -1

# x or y # truthy because y is -1 which is a nonzero value( (0) false x (-1) false);

#  x - 1 == y # true because x - 1 is -1, ((-1) false x false(-1))

# x or y and x - 1 == y # true because both sides of the AND are truthy;((0)false x (-1)false)

# y + 1 == x # truthy because -1 + 1 does in fact equal zero;(-2(false) x 0(false)) 

# x or y and x - 1 == y and y + 1 == x # also truthy because both sides of the second AND are truthy

x or y and x - 1 == y and y + 1 == x


a = -1
not a  # this expression
# Negative numbers are just like regular numbers, so not (True) is false
