'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''
def partition(l1,f1):
    truthy_list = []
    falsy_list = []
    for v in l1:
        if f1(v):
            truthy_list.append(v)
        else:
            falsy_list.append(v)
    return [truthy_list,falsy_list]


def isEven(num):
    return num % 2 == 0

print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]]
