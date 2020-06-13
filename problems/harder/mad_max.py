# https://binarysearch.io/question/16
from collections import deque


class Solution:
    def solve(self, nums, k):
        d = deque()
        r = []
        n = len(nums)
        for i in range(n):
            while d and d[0][1] <= i - k:
                d.popleft()
            while d and d[-1][0] <= nums[i]:
                d.pop()
            d.append([nums[i], i])
            if k - 1 <= i:
                r.append(d[0][0])

        return r


s = Solution()
assert s.solve([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
assert s.solve([1, 2, 3, 4, 5, 4, 3, 2, 1], 3) == [3, 4, 5, 5, 5, 4, 3]
assert s.solve([3, 2, 1, 2, 3], 2) == [3, 2, 2, 3]
assert s.solve([3, 2, 1, 2, 3], 5) == [3]
