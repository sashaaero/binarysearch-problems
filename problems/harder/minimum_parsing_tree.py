# https://binarysearch.io/question/433


class Solution:
    def solve(self, bp):
        from functools import lru_cache
        @lru_cache(None)
        def op(i, j):
            if j == i + 1:
                return bp[j] - bp[i]
            min_val = min(op(i, k) + op(k, j) for k in range(i+1, j))
            return min_val + bp[j] - bp[i]
        return op(0, len(bp)-1)


s = Solution()
assert s.solve([0, 5, 8, 9]) == 22