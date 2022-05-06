# FIRST EXAMPLE:
import pdb #-> python debugger
first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)