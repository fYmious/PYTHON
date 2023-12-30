def solution(s: str) -> list:
    s = s + "_" if len(s) % 2 != 0 else s
    res: list[str] = []
    for i in range(0, len(s) - 1, 2):
        res.append(f"{s[i]}{s[i + 1]}")

    return res


print(solution("abc"))
