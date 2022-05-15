'''
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''

UDEMY
def includes(item,val,start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]
'''

def repeat(string_in, repeat_in):
    return string_in * repeat_in

print(repeat('*', 3)) # '***' 
print(repeat('abc', 2)) # 'abcabc' 
print(repeat('abc', 0)) # ''    