
x = 1
num1 = 3 * 9 ** (x ** 2 - 2 * x)
num2 = 84 * 12 ** (x ** 2 - 2 * x - 1)
num3 = 4 * 16 ** (x ** 2 - 2 * x)

print(num1 - num2 + num3 == 0)