l1 = [-1,2,3,-4]
l2 = [-1,"a",3,-4]
l3 = ["a","friend"]

def is_all_strings(l1): 
    return all([isinstance(x, str) for x in   l1 ])

    #return list(type(x) for x in l1 )

print(is_all_strings(l1))
print(is_all_strings(l2))
print(is_all_strings(l3)) 

#udemy
def is_all_strings(lst):
    return all(type(l) == str for l in lst)