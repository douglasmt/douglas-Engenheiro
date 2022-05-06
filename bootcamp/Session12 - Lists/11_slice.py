sounds = ["super", "ali", "docious", "fight","removeme", "removeme"]
print(sounds[2:])
print(sounds[2:2])
print(sounds[2:3])
print(sounds[:])
print(sounds[:2])
print(sounds[:3])
#['super', 'ali', 'docious']
sou2 = sounds[:]
print(sou2 == sounds)
#True
print(sou2 is sounds)
False
print( sou2[:-1])
#['super', 'ali', 'docious', 'fight', 'removeme']
print( sou2[:-2])
#['super', 'ali', 'docious', 'fight']
print(sou2[2:-2])
#['docious', 'fight']
print(sou2[2:-3])
#['docious']
print(sou2[2:-1])
#['docious', 'fight', 'removeme']
print(sou2[:])
#['super', 'ali', 'docious', 'fight', 'removeme', 'removeme']
print(sou2[:1:-1])
#['removeme', 'removeme', 'fight', 'docious']
print(sou2[2::-1])
#['docious', 'ali', 'super']

print(sou2[5][::-1])
#'emevomer'

