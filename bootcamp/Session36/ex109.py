'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''

def list_check(list_par):
    for i in list_par:
        if not isinstance(i, list):
            return False
    return True

'''UDEMY
list_check

def list_check(vals):
    return all(type(l) == list for l in vals)

'''