from itertools import product

def check(num: tuple[int]) -> bool:
    for i in range(len(num) - 1):
        if (num[i] + num[i + 1]) % 2 == 0:
            return False

    return True


counter: int = 0
for i in product([0, 1, 2, 3, 4, 5], repeat=5):
    if i[0] != 0:
        if check(i):
            counter += 1

print(counter)

