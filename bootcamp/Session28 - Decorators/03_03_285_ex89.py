# Let's define a speed_test decorator
from functools import wraps
from time import time

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        #result = fn(*args, **kwargs) 
        arguments = tuple(x for x in args)
        kwarguments = {k:v for k,v in kwargs.items()}

        print("Here are the args: {}".format(arguments))
        print("Here are the kwargs: {}".format(kwarguments))
		
        #return result
    return wrapper

@show_args
def do_nothing(*args,**kwargs):
	pass	


print(do_nothing(1,2,3,a="hi",b="bye"))


'''UDEMY
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)
Here's the complete code:

from functools import wraps
 
def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)
    return wrapper
'''