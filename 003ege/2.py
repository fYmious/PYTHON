from itertools import *


def f(x, y, w, z, u):
    return ((z <= w) and (y == (not x))) <= (u == (y or z))


for a1, a2, a3, a4, a5, a6, a7, a8 in product([0, 1], repeat=8):
    t = [(0, a1, 0, 0, 0),
         (0, a2, a3, 0, 0),
         (a4, 0, 0, 0, a5),
         (0, 0, a6, a7, a8)]

    if len(t) == len(set(t)):
        for p in permutations("xywzu"):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0, 0]:
                print(p)
