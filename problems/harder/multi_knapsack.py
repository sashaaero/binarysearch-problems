# https://binarysearch.io/question/583
from functools import lru_cache


class Solution:
    def solve(self, weights, values, cap, count):
        data = list(zip(weights, values))
        data.sort(key=lambda e: e[1] / e[0], reverse=True)
        size = len(data)
        max_val = 0
        @lru_cache(None)
        def op(i, left_cap, cnt):
            if cnt == 0 or i == size:
                return 0

            w, v = data[i]
            max_val = op(i+1, left_cap, cnt)
            if left_cap >= w:
                max_val = max(max_val, op(i+1, left_cap-w, cnt-1) + v)
            return max_val

        return op(0, cap, count)


s = Solution()
assert s.solve([1, 1, 3, 5], [10, 10, 20, 30], 5, 3) == 40
assert s.solve([1, 1, 3, 5], [10, 10, 20, 30], 5, 2) == 30
assert s.solve([1, 1, 3, 5], [10, 10, 20, 30], 100, 3) == 60

