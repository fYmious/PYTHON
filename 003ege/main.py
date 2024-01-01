def to_any(num: int, base: int = 3) -> list:
    translate: dict = {1: "1",
                       2: "2",
                       3: "3",
                       4: "4",
                       5: "5",
                       6: "6",
                       7: "7",
                       8: "8",
                       9: "9",
                       10: "A",
                       11: "B",
                       12: "C",
                       13: "D",
                       14: "E",
                       15: "F"}
    res: list[int] = []
    while num > 0:
        res.append(translate[num % base])
        num //= base

    return res[::-1]


def task(n: int) -> int:
    third: list[str] = to_any(n)
    if len(third) % 2 != 0:
        third = ["1"] + third

    if sum(int(i) for i in third):
        third = third + third[:2]
    else:
        remainder: list[str] = to_any(n % 5)
        third = third + remainder

    third = list(str(int("".join(third))))

    if third[0] == "2":
        third = third[1:]

    if third[-1] == third[-2]:
        third = third[:-1]

    return int("".join(third), 3)


print(task(14))