class Solution:
    def solve(self, s):
        res = cur_len = 1
        cur_char = s[0]
        for i, n in enumerate(s):
            if i == 0: continue
            if cur_char == n:
                cur_len += 1
                res += cur_len - 1
            else:
                cur_char = n
                cur_len = 1

            res += 1
        return res


s = Solution()
assert s.solve("aab") == 4
