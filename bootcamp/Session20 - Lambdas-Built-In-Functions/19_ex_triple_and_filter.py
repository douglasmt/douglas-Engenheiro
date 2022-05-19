def triple_and_filter(l1):
    return [ x * 3 for x in ( list(filter(lambda x : x % 4 == 0, l1)) ) ]
    
# udemy
'''    
def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))
'''

l1 = [1,2,3,4]
print(triple_and_filter(l1))
print(triple_and_filter([6,8,10,12]))