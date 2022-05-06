l1 = [-1,2,3,-4]

def remove_negatives(l1): 
    return list(filter(lambda x : x >= 0, l1))

print(remove_negatives(l1))