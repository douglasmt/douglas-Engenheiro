names = [2,3,22, 312,2,3,321,12,534,34]
print(names.index(534,2,9)) 
# looks for 534 from index 2(number 22) to 9(number 34)

print(names.index(12,2,8)) 
# looks for 312 from index 2(number 22) to 8(number 534)

print(names.index(34,2,10)) 
# looks for 312 from index 2(number 22) to 10(end of the list)

print(names.index(22,2)) 
# looks for 312 from index 2(number 22) 
