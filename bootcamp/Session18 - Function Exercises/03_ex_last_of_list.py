'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(list_elements):
    if list_elements:
        return list_elements[-1]
    else:
        return None

print(last_element([1,2,3])) # 3
print(last_element([])) # None        