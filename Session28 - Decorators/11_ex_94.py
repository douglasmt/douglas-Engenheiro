'''
@delay(3)
def say_hi():
    return "hi"

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"
'''

from functools import wraps
from time import sleep

def delay(tempo):
    def decorator(fn):
        def new_func(*args, **kwargs):
            print("Waiting 3s before running say_hi")
            sleep(tempo)
            return fn(*args, **kwargs)
        return new_func
    return decorator


@delay(3)
def say_hi():
    return "hi"

print(say_hi())