
def intersection(l1,l2):
    return [v for v in l1 if v in l2]


print(intersection([1,2,3,4] , [3,4,5,6]))

'''Manual Looping Solution
Here's one potential solution:

Define an empty list that will eventually store the in common values
Loop through one list (l1)
For each value, check if that value is in the other list (l2)
If it is, append the value to the in_common list
Return in_common  after the loop ends'''
'''def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common'''
    
    