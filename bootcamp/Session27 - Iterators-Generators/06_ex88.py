def get_unlimited_multiples(mul=1):
    next_num = mul
    while True:
        yield next_num
        next_num += mul

sevens = get_unlimited_multiples(7)
[print(next(sevens)) for i in range(15)] 

