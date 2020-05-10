# https://binarysearch.io/question/85

class Solution:
    def solve(self, nums, k):
        dp = [-1 for _ in range(k)]
        dp[0] = 0
        for n in nums:
            tmp = dp[:]
            for i in range(k):
                if dp[i] == -1: continue
                j = (i + n) % k
                tmp[j] = max(tmp[j], dp[i] + n)
            dp = tmp
        return dp[0]


s = Solution()
assert s.solve([2, 6, 4, 1], 1) == 13
assert s.solve([5], 2) == 0
assert s.solve([3, 8, 5, 6, 1], 3) == 18
