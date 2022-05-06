def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None

print(return_day(1)) # "Sunday"
print(return_day(2)) # "Monday"
print(return_day(3)) # "Tuesday"
print(return_day(4)) # "Wednesday"
print(return_day(5)) # "Thursday"
print(return_day(6)) # "Friday"
print(return_day(7)) # "Saturday"
print(return_day(41)) # None        