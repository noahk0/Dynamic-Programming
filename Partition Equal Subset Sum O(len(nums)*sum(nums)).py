def canPartition(self, nums: List[int]) -> bool:
    half = sum(nums)

    if half % 2:
        return False

    half //= 2

    if half in nums:
        return True

    if half < max(nums):
        return False

    seen = {0}

    for num in nums:
        if half - num in seen:
            return True
            
        seen.update({n + num for n in seen})
