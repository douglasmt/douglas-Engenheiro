from functools import wraps

def ensure_fewer_than_three_args(fn):
	@wraps(fn)
	def wrapper(*args):
		if len(args) > 2:
			return "Too many arguments!"
		return fn(*args)
	return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

print(add_all()) # 0
print(add_all(1)) # 1
print(add_all(1,2)) # 3
print(add_all(1,2,3)) # "Too many arguments!"
print(add_all(1,2,3,4,5,6)) # "Too many arguments!"

'''
UDEMY
Ensure Fewer Than Three Args Decorator Solution
from functools import wraps
 
def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return fn(*args, **kwargs)
        return "Too many arguments!"
    return wrapper
    '''
