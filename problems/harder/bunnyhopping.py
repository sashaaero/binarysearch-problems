# https://binarysearch.io/question/538
from heapq import heappush, heappop


class Solution:
    def solve(self, nums, k):
        size = len(nums)
        dp = [0] * size
        d = []
        for i, n in enumerate(nums):
            v = None
            while d:
                v, j = d[0]
                if j >= i - k: break
                heappop(d)
            if v:
                dp[i] = nums[i] + v
            else:
                dp[i] = nums[i]
            heappush(d, (dp[i], i))

        return dp[size - 1]


s = Solution()
assert s.solve([1, 2, 3, 4, 5], 2) == 9