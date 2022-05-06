def extremes(iterable):
    minimo = min(n for n in iterable) # 3
    
    # find the longest name itself
    maximo = max(n for n in iterable)

    return (minimo,maximo)

print(extremes([1,2,3,4,5]))
print(extremes([99,25,30,-7]))
print(extremes("alcatraz"))

# udemy
def extremes(nums):
    return(min(nums), max(nums))