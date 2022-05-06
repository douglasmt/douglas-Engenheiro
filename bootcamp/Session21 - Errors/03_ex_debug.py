def divide(num1,num2):
    try:
        result = num1/num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    else:
        return int(result)

#divide(1,'a')
print(divide(4,2))
#print(divide([],"1"))  #"Please provide two integers or floats"
#print(divide(1,0))  #"Please do not divide by zero"


'''
ALWAYS RETURN THE MESSAGE!
def divide(num1,num2):
    if (type(num1) is not int or type(num2) is not int) or (type(num1) is not int or type(num2) is not int):
        raise TypeError("Please provide two integers or floats")
    if num2 == 0:
        raise ZeroDivisionError("Please do note divide by zero")
    result = num1/num2
    print(int(result))'''