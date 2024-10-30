def longestPalindrome(self, s: str) -> str:
    string = ' ' + ' '.join(s) + ' '
    center, longest, leng = 0, 0, [0] * len(string)

    for i in range(1, len(string)):
        if i < center + leng[center]:
            leng[i] = min(center + leng[center] - i, leng[center * 2 - i])

        while leng[i] + 1 < min(i + 1, len(string) - i) and string[i + leng[i] + 1] == string[i - leng[i] - 1]:
            leng[i] += 1

        if leng[longest] < leng[i]:
            longest = i

        if len(string) <= i + leng[longest]:
            return s[(longest - leng[longest]) // 2 : (longest + leng[longest]) // 2]

        if center + leng[center] < i + leng[i]:
            center = i
