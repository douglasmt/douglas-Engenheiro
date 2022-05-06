def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David! Please say {kwargs['Heather']}"

    return "Not sure who this is..."

# print(special_greeting(David='Hello')) # Hello David!
# print(special_greeting(Bob='hello')) # Not sure who this is...
# print(special_greeting(David='special')) # You get a special greeting David!

# print(special_greeting(Heather="hello", David="special"))
print(special_greeting(Bob='hello', David='special', Heather="hello"))
print(special_greeting(Bob='hello', David='not at all', Heather="hello"))
print(special_greeting(Bob='hello')) # Not sure who this is...
