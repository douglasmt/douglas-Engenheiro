# This version only accepts one argument
def shout(fn):
    def wrapper(name):
        return fn(name).upper()
    return wrapper

@shout
def greet(name):
    return f"Hello {name}."

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."


print(greet("Johnny"))

print(order("fries","coke"))
"""     print(order("fries","coke"))
TypeError: wrapper() takes 1 positional argument but 2 were given
 """