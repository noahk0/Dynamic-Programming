def countSubstrings(self, s: str) -> int:
    string = ' ' + ' '.join(s) + ' '
    res, center, leng = 0, 0, [0] * len(string)

    for i in range(1, len(string)):
        if i < center + leng[center]:
            leng[i] = min(center + leng[center] - i, leng[center * 2 - i])

        while leng[i] < min(i + 1, len(string) - i) and string[i + leng[i]] == string[i - leng[i]]:
            leng[i] += 1

        res += leng[i] // 2

        if center + leng[center] < i + leng[i]:
            center = i

    return res
