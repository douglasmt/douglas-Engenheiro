'''
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''

def three_odd_numbers(nums):
    
    i2 = 0
    i3 = 0
    for i in range(0,len(nums)):
        if (i+2) == len(nums):
            break
        sum_3 = nums[i] + nums[i+1] + nums[i+2]
        if sum_3 %2 != - 0:
            return True
    return False

print(three_odd_numbers([1,2,3,4,5]))
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0]))
print(three_odd_numbers([5,2,1]))
print(three_odd_numbers([1,2,3,3,2]))