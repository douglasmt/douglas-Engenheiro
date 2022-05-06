'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

def calculate(**kwargs):

    if kwargs["operation"] == 'add':
        result = kwargs["first"] + kwargs["second"]
    elif kwargs["operation"] == 'subtract':
        result = kwargs["first"] - kwargs["second"]
    elif kwargs["operation"] == 'multiply':
        result = kwargs["first"] * kwargs["second"]
    elif kwargs["operation"] == 'divide':
        result = kwargs["first"] / kwargs["second"]

    if "message" in kwargs:
        message = kwargs["message"] 
    else:
        message = "The result is"

    if kwargs["make_float"]:
        return message + " " + str(float(result))
    else:
        return message + " " + str(int(result))

print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
print(calculate(make_float=True, operation='subtract', message='You just subtracted', first=2, second=4))

