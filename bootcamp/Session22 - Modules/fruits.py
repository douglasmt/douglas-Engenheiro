# Importing everythin in both modules:

# import bananas
# import apples

# print(apples.offer())

# print(bananas.dip_in_chocolate())


# Importing a single function from bananas:
from bananas import dip_in_chocolate as dip
print(dip())

from apples import offer as off
print(off())

import apples

from bananas import peel as pe
print(pe())