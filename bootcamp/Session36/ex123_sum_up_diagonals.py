'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
sum_up_diagonals(list2) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
sum_up_diagonals(list4) # 68
'''

# def sum_up_diagonals(diag):
#     diag_sum = 0
#     i = 0
#     j = 0
#     for i  in range(len(diag)):
#         print(diag[i][i])
#         #i += 1
#         diag_sum += diag[i][i]
#     i_c = 0
#     for i  in range(len(diag)):
#         i_c = len(diag) - i - 1
#         i_r = 0 + i 
#         print("o número {},{} é {}".format(i_c,i_r, diag[i_c][i_r]))
#         diag_sum += diag[i_r][i_c]

#     return 'A soma é ' + str(diag_sum)
def sum_up_diagonals(diag):
    diag_sum = 0
    i = 0
    j = 0
    for i  in range(len(diag)):       
        diag_sum += diag[i][i]
    i_c = 0
    for i  in range(len(diag)):
        i_c = len(diag) - i - 1
        i_r = 0 + i 
        diag_sum += diag[i_r][i_c]

    return diag_sum


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
print(sum_up_diagonals(list1)) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
print(sum_up_diagonals(list2)) # 30

list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

print(sum_up_diagonals(list3)) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
print(sum_up_diagonals(list4)) # 68