sounds = ["super", "ali", "docious"]

sounds.append(["!!!","asasda"])
print(sounds)
print(len(sounds))
9
sounds.extend(["extension!!!","right"])
print(sounds)
sounds.insert(1,"SUPERWORD")
print(sounds)

sounds.insert(-1,"ENDWORD")
print(sounds)

sounds.insert(len(sounds)," ---- ENDWORD")
print(sounds)
