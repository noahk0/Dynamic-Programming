def rob(self, nums: List[int]) -> int:
    cur1 = cur2 = pre1 = pre2 = 0

    for i in range(1, len(nums)):
        pre1, pre2, cur1, cur2 = cur1, cur2, max(cur1, nums[i] + pre1), max(cur2, nums[i - 1] + pre2)

    return max(cur1, cur2, nums[0])
