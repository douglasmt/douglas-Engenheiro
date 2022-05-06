'''
iterator - you make next to iterate upon it

iterable - list is but a string is if you make as
iter("HELLO")
'''

name = "Ophrah"
iter(name)
#<str_iterator object at 0x7fe09a408890>
it = iter(name)
next(it)
#'O'
next(it)
#'p'
next(it)
#'h'
next(it)
#'r'
next(it)
#'a'
next(it)
#'h'
#next(it)
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> '''