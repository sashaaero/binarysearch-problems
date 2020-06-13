class Solution:
    def solve(self, s, t):
        len_diff = len(s) - len(t) + 1
        n = len(t)
        t = list(t)
        min_diff = 101
        for i in range(len_diff):
            cur_diff = 0
            for j in range(n):
                if s[i+j] != t[j]:
                    cur_diff += 1
            min_diff = min(min_diff, cur_diff)

        return min_diff if min_diff < 101 else 0


s = Solution()
assert s.solve("foobar", "oops") == 2
assert s.solve("zcq", "zq") == 1
assert s.solve("a", "q") == 1
assert s.solve("zkv", "kvq") == 3

