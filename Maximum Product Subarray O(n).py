def maxProduct(self, nums: List[int]) -> int:
    res = biggest = smallest = nums[0]

    for n in nums[1:]:
        biggest, smallest = max(n, n * biggest, n * smallest), min(n, n * biggest, n * smallest)
        res = max(res, biggest)

    return res
