def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        count += 1
        return count
    print(count) # first count declared
    return inner()

print(outer())