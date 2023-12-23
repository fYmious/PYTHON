from itertools import product, permutations


def f(x, y, z, w):
    return not (z <= w) or (x <= y) or (not z)


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(0, a1, a2, 0),
             (1, 0, a3, a4),
             (a5, 1, a6, a7)]

    if len(set(table)) == len(table):
        for permutation in permutations("xyzw"):
            if [f(**dict(zip(permutation, row))) for row in table] == [0, 0, 0]:
                print(permutation)
