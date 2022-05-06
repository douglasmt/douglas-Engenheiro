artist2 = {
    "first": "Paul",
    "last": "McCartney",
    "band": "Beatles",
}
 
full_name2 = f"{artist2['first']} {artist2['last']} from the band {artist2['band']}"
print(full_name2)

print("\n KEYS: \n")
for value in artist2.values():
    print(value)

print("\n VALUES: \n")
for v in artist2.keys():
    print(v)

print("\n  KEYS AND VALUES: \n")
for k,v in artist2.items():
    print(f"Key is {k} and value is {v}")

