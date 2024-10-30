def climbStairs(self, n: int) -> int:
    cur = pre = 1

    for _ in range(1, n):
            pre, cur = cur, cur + pre

    return cur
