from bisect import bisect_left




class Solution:
    def solve(self, nums):
        def lis(nums, lo, hi):
            dp = []
            for k in range(lo, hi):
                x = nums[k]
                hi = bisect_left(dp, x)
                if hi >= len(dp):
                    dp.append(x)
                else:
                    dp[hi] = x
            return len(dp)

        a = nums
        b = nums[::-1]
        n = len(a)
        res = 0
        for i in range(len(nums)):
            #print(a[0:i+1], b[0:n-i-1])
            res = max(res, lis(a, 0, i + 1) + lis(b, 0, n - i - 1))
        return res


s = Solution()
print(s.solve([1, 0, 3, 2, 9, 4, 5, 2]))
print(s.solve([1, 3, 2, 5, 9]))
print(s.solve([549, 201, 137]))
