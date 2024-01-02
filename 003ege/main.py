from itertools import permutations, product

def check(num: tuple[int]) -> bool:
    for i in range(len(num) - 1):
        if (num[i] + num[i + 1]) % 2 == 0:
            return False

    return True

counter: int = 0
for i in product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], repeat=3):
    if len(set(i)) == len(i):
        if check(i):
            counter += 1

print(counter)