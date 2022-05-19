'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(n1,n2):
    if n1 > n2:
        return 'First is greater'
    elif n1 < n2:
        return 'Second is greater'
    else:
        return 'Numbers are equal'

print(number_compare(1,1) )
print(number_compare(1,0) )
print(number_compare(2,4) )

