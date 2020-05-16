from collections import Counter


class Solution:
    def solve(self, nums):
        size = len(nums)
        r = [0] * size
        c = Counter(nums)
        for k, v in c.items():
            for i in range(size):
                if k > i: r[i] += v
        return r == nums



s = Solution()
assert s.solve([7, 4, 3, 2, 1, 1, 1]) == True
assert s.solve([5, 3, 2, 1, 1]) == True