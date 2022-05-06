'''
@only_ints 
def add(x, y):
    return x + y
    
add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''

from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args): 
        for x in args:
            if not isinstance(x, int):                
                return "Please only invoke with integers."               
            else:
                return fn(*args)
            
    return wrapper

# modificando para ficar como o UDEMY
# def only_ints(fn):
#     @wraps(fn)
#     def wrapperao(*args): 
#         for x in args:
#             if type(x) != int:
#                 return "Please only invoke with integers."               
#             else:
#                 return fn(*args)
            
#     return wrapperao

''' ficou estranho
def only_ints(fn):
    @wraps(fn)
    def wrapperao(*args): 
        if any([ x for x in args if isinstance(x, int)]): 
            return "Please only invoke with integers."               
        else:
            return fn(*args)            
    return wrapperao    
'''


@only_ints 
def add(x, y):
    return x + y

print(add(1, 2)) # 3
print(add("1", "2"))
