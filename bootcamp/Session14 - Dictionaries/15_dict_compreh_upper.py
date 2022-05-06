artist2 = {
    "first": "Paul",
    "last": "McCartney",
    "band": "Beatles",
}
kv_upper = {(k.upper() if k is 'band' else k): v for k,v in artist2.items()}
print(kv_upper)