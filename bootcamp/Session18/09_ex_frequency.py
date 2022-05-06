

def frequency(l1,search_term):
    return l1.count(search_term)
    #return [l1.count(search_term) for v in l1 if l1[v] == search_term]

print(frequency([1,2,3,4,4,4], 4)) # 3
print(frequency([True, False, True, True], False)) # 1