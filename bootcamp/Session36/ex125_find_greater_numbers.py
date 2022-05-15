'''
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''

# def find_greater_numbers(nums):
#     #print(nums[-1])
#     for i in range(0,len(nums)):
#         print("começando a comparar o {}".format(nums[i]))
#         for j in range(i,len(nums)):
#             print("{}<{}?={}".format(nums[i],nums[j],nums[i]<nums[j]))

def find_greater_numbers(nums):
    sum_greater = 0
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if nums[i]<nums[j]: 
                sum_greater += 1

    return sum_greater
    
            
 

print(find_greater_numbers([1,2,3])) # 3 
print(find_greater_numbers([6,1,2,7])) # 4
print(find_greater_numbers([5,4,3,2,1])) # 0
print(find_greater_numbers([])) # 0