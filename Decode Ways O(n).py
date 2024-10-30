def numDecodings(self, s: str) -> int:
    if not int(s[0]):
        return 0

    cur = pre = 1

    for i in range(1, len(s)):
        tmp = cur

        if s[i] == '0':
            cur = 0

        if s[i - 1] == '1' or s[i - 1] == '2' and int(s[i]) < 7:
            cur += pre

        pre = tmp

    return cur
