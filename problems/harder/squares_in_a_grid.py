class Solution:
    def solve(self, r, c):
        mod = 10 ** 9 + 7
        def op(cur, i):
            if i == min(r, c):
                return cur % mod
            return op(cur + ((r - i) * (c - i) * i), i+1)

        return op(0, 0) % mod


s = Solution()
assert s.solve(2, 2) == 1
assert s.solve(3, 3) == 6
assert s.solve(9, 9) == 540