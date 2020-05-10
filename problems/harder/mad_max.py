# https://binarysearch.io/question/16
from collections import deque


class Solution:
    def solve(self, nums, k):
        d = deque(nums[:k])
        r = [max(d)]
        for i in range(k, len(nums)):
            d.popleft()
            d.append(nums[i])
            r.append(max(d))
        return r


s = Solution()
assert s.solve([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
assert s.solve([1, 2, 3, 4, 5, 4, 3, 2, 1], 3) == [3, 4, 5, 5, 5, 4, 3]
assert s.solve([3, 2, 1, 2, 3], 2) == [3, 2, 2, 3]
assert s.solve([3, 2, 1, 2, 3], 5) == [3]
