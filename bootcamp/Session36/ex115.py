'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''
# 
def includes(item,val,start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]
    
#print(includes([1, 2, 3], 1)) # True 
#print(includes([1, 2, 3], 1, 2)) # False 
#print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
#print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False

# def includes(coll, value, ind=''):
#     if ind != '':
#         if value == coll[ind]:                
#             return True
#     elif isinstance(coll, list) or isinstance(coll, str):
#         if value in coll:
#             return True
#     elif isinstance(coll, dict):
#         for val in coll.values():
#             if val == value:
#                 return True  
#     return False

'''UDEMY
def includes(item,val,start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]

'''


