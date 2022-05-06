from numpy import subtract


def add(a):
    return a+90

def subtract1(a):
    return a-200


def teste(par1=0, par2="Michael", fn=add):
    if par1 > 1 or par2 == "Michael":
        print(f"Excellent ")
        return fn(par1)
    else:
        print("Wrong answer")
        return subtract1(par1)


print(teste(0,"jorge"))
print(teste(90))
print(teste(90,"jorge"))