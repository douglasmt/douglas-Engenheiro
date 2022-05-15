'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 

UDEMY
def remove_every_other(lst):
    return [val for i,val in enumerate(lst) if i % 2 == 0]
'''

def remove_every_other(one_list):
    new_one_list = []
    other = True
    for i in one_list:
        if other:
            new_one_list.append(i)
            other = False
        else:
            other = True        
    return new_one_list

print(remove_every_other([1,2,3,4,5])) # [1,3,5] 
print(remove_every_other([5,1,2,4,1])) # [5,2,1]
print(remove_every_other([1]))