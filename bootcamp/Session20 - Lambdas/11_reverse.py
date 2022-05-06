listinha = [1,2,3,4,5]
print(list(reversed(listinha)))
print(listinha)
print("alcatraz"[::-1])
print(''.join(list(reversed("alcatraz"[::-1])))) # reverse(zartacla) reversed(alcatraz)

for x in reversed(range(0,10)):
    print(x)