from itertools import permutations

counter: int = 0
for i in set(permutations("ВОДОПАД")):
    word = ''.join(i)
    for l in "ОА": word = word.replace(l, '1')
    if "11" not in word:
        counter += 1

print(counter)

