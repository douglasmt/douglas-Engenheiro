'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}

UDEMY
def two_list_dictionary(keys, values):
    collection = {}
 
    for idx, val in enumerate(keys):
        if idx < len(values):
            collection[keys[idx]] = values[idx]
        else:
            collection[keys[idx]] = None
 
    return collection
'''

from sqlalchemy import null


def two_list_dictionary(keys,values):
    dict_out = {}
    for i in range(0,len(keys)):
        
        if i < len(values):
            print(values[i])
            dict_out[keys[i]] = values[i]
        else:
            dict_out[keys[i]] = None

    #for  i in range(0,len(keys)):
    #    dict_out = dict(keys[i]=values[i])
    #dict_out = {keys[i]:values[i]  for i in range(0,len(keys)) }
    # dict_out = {pair for pair in zip(keys,values)}
    return dict_out

print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))    
print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4])) # {'a': 1, 'b': 2, 'c': 3}
print(two_list_dictionary(['x', 'y', 'z']  , [1,2])) # {'x': 1, 'y': 2, 'z': None})