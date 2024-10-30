def lengthOfLIS(self, nums: List[int]) -> int:
    seq = [nums[0]]

    for n in nums[1:]:
        if seq[-1] < n:
            seq.append(n)
        else:
            seq[bisect_left(seq, n)] = n

    return len(seq)
