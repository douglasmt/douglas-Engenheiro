num_list = range(1,12)

even_list = {num:("even" if num % 2 == 0 else "odd") for num in num_list}

print(even_list)