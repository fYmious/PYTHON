def factorial(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(35))
