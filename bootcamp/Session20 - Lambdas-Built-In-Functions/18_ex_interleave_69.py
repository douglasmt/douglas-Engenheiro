'''
def interleave(st1,st2):
    zst = list(zip(st1,st2))
    l1 = "".join(zst[0])
    l2 = "".join(zst[1])
    lall = l1 + l2
    return lall
'''

def interleave(st1,st2):
    zipado = list(zip(st1,st2))
    print(zipado)
    return ''.join(''.join(x) for x in zipado)
    # [('h', 'h'), ('i', 'a')] is returned together as 'hhia'
    # [('l', 'i'), ('z', 'a'), ('r', 'd')] is returned together as 'lizard'


print(interleave('hi', 'ha'))
print(interleave('aaa', 'zzz'))
print(interleave('lzr', 'iad'))