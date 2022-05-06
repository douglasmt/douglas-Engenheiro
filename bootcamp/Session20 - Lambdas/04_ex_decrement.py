
lista = [1,3,7,8]

decrement_list = list(map(lambda a: a - 1, lista ) )
# Executing the lambdas
print(list(decrement_list))

def decrement_list(l):
    return list(map(lambda a: a - 1, l ) )