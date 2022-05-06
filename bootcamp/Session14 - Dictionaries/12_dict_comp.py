st1 = ["ABC"]
st2 = ["123"]
combo = {st1[i] : st2[i] for i in range(0,len(st1)) }

print("list with ABC item")
print(combo)

st1 = "ABC"
st2 = "123"
combo = {st1[i] : st2[i] for i in range(0,len(st1)) }
print("list with ABC string")
print(combo)
