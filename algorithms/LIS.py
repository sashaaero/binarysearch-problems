# nlogn

from bisect import bisect_left

def lis(nums, i, j):
    dp = []
    for k in range(i, j):
        x = nums[k]
        j = bisect_left(dp, x)
        if j >= len(dp):
            dp.append(x)
        else:
            dp[j] = x
    return len(dp)
