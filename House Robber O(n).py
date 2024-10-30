def rob(self, nums: List[int]) -> int:
    cur = pre = 0

    for n in nums:
        pre, cur = cur, max(cur, n + pre)
            
    return cur
