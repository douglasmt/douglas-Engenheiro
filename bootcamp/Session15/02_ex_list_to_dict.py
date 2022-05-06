from multiprocessing.connection import answer_challenge


person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
print(person)
# use the person variable in your answer
answer = {k:v for k,v in person}
print(answer)

# thing will be each data such as ["name", "Jared"]
answer2 = {thing[0]: thing[1] for thing in person}
print(answer2)

answer3 = dict(person)
print(answer3)