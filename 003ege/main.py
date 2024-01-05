def f(n, a, b):
    x = 9 + n * (a + 11) - 58
    y = -10 + n * (b + 9) - 18
    return x == 0 and y == 0


for n in range(1000):
    if any([f(n, a, b) for a in range(-150, 150) for b in range(-150, 150)]):
        print(n)
        break
