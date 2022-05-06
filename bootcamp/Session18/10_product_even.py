'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(nums):
    mult = 1 
    for n in nums:
        if n % 2 == 0:
            mult *= n
    return mult 

print(multiply_even_numbers([2,3,4,5,6])) # 48

