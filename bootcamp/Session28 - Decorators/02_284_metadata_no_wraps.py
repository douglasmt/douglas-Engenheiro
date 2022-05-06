#from functools import wraps
def log_function_data(fn):
    #@wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}") # add
        print(f"Here's the documentation: {fn.__doc__}") # Adds two ...
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x,y):
    """Adds two numbers together."""
    return x + y

print(add.__doc__)
print(add.__name__)

'''
print(add.__doc__)
add.doc will print the "Adds two ....", the doc of add function
    """Adds two numbers together."""

print(add.__name__)
add'''

print("\n Now the numbers \n")
print(add(1,2))
'''
you are about to call add
Here's the documentation: Adds two numbers together.
3
'''

#help(add)
'''
without the import wraps will show this at help(add) function:
I AM WRAPPER FUNCTION
'''