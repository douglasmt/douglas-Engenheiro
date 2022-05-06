name = 'Colt'
print([char.upper() for char in name])
print(name.upper())

friends = ['colt','matt','debora']
print([each_one.upper() for each_one in friends])
print([each_one[0].upper() + each_one[1:] for each_one in friends])