midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

final_grades = [pair for pair in zip(midterms,finals)]

print(final_grades)

final_grades = [max(pair) for pair in zip(midterms,finals)]

print(final_grades)

final_grades = {t[0]:max(t[1],t[2]) for t in zip(students,midterms,finals)}

print(final_grades)

scores = map(
    lambda pair: max(pair),
    zip(midterms,finals)
)
print(list(scores))


final_scores = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms,finals)
        )
    )
)
print(final_scores)