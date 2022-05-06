def get_multiples(num=1,count=10):
    i = 0
    while i < count:        
        i+=1
        yield num * i
     
""" 
UDEMY
def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num """

#evens = get_multiples(2,3)
default_multiples = get_multiples()
print(list(default_multiples))

evens = get_multiples(2,3)
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))

