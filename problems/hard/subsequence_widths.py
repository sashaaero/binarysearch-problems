class Solution:
    def solve(self, nums):
        nums.sort()
        size = len(nums)
        dp = [1]
        for i in range(1, size):
            dp.append(dp[-1] * 2)
        res = 0
        for i, n in enumerate(nums):
            res = res + (dp[i] - dp[size - 1 - i]) * n
        return res % (10 ** 9 + 7)

s = Solution()
assert s.solve([6, 3, 8]) == 15