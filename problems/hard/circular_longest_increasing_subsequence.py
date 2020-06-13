from bisect import bisect_left

class Solution:
    def solve(self, nums):
        n = len(nums)
        nums = nums + nums

        def longest(i, j):
            dp = []
            for k in range(i, j):
                x = nums[k]
                j = bisect_left(dp, x)
                if j >= len(dp):
                    dp.append(x)
                else:
                    dp[j] = x
            return len(dp)

        return max(longest(i, i + n) for i in range(n))


s = Solution()
assert s.solve([5, 4, 7, 1, 2, 3]) == 5
assert s.solve([10, 3, 1, 3, 0, 3, 14, 15, 5, 9, 14, 13, 2, 10, 10, 2, 12]) == 6
