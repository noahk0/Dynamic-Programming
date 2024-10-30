def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    dp = [True] + [False] * len(s)

    for i in range(1, len(s) + 1):
        for w in wordDict:
            if len(w) <= i and w == s[i - len(w): i]:
                dp[i] = dp[i - len(w)]

                if dp[i]:
                    break

        return dp[-1]
