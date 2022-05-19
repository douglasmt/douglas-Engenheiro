def return_day(num):
    if num == 1:
        return ("Sunday")
    elif num == 2:
        return ("Monday")
    elif num == 3:
        return ("Tuesday")
    elif num == 4:
        return ("Wednesday")
    elif num == 5:
        return ("Thursday")
    elif num == 6:
        return ("Friday")
    elif num == 7:
        return ("Saturday")
    else:
        return None
    
print(return_day(1)) # "Sunday"
print(return_day(2)) # "Monday"
print(return_day(3)) # "Tuesday"
print(return_day(4)) # "Wednesday"
print(return_day(5)) # "Thursday"
print(return_day(6)) # "Friday"
print(return_day(7)) # "Saturday"
print(return_day(41)) # None
