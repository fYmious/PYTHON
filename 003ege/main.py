def f(s, m):
    if s >= 13: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 2, m - 1), f(s + 5, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)

print("П1", [s for s in range(13) if f(s, 1)])
print("В1", [s for s in range(13) if f(s, 2)])
print("П2", [s for s in range(13) if f(s, 3)])
print("В2", [s for s in range(13) if f(s, 4)])
print("П3", [s for s in range(13) if f(s, 5)])
print("В3", [s for s in range(13) if f(s, 6)])

