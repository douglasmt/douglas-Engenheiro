import re as rege
def parse_bytes(str_bin):
    bin_regex = rege.compile(r'\b((0|1)(0|1)(0|1)(0|1)(0|1)(0|1)(0|1)(0|1))\b')
    return bin_regex.findall(str_bin)
    #match.group()

print(parse_bytes("11010101 101 323"))
print(parse_bytes("My data is: 10101010 11100010"))
print(parse_bytes("asdas"))
