class Solution:
    def solve(self, s0, s1):
        s0 = list(s0)
        s1 = list(s1)
        def _(s0, s1, i):
            if i >= len(s0):
                return 0
            if s0[i] == s1[i]:
                return _(s0, s1, i+1)

            char = s1[i]
            candidates = []
            for j in range(i, len(s0)):
                if s0[j] == char:
                    candidates.append(j)

            swaps = 1e9
            for j in candidates:
                tmp = s0[:]
                tmp[i], tmp[j] = tmp[j], tmp[i]
                swaps = min(swaps, _(tmp, s1, i+1) + 1)

            return swaps

        return _(s0, s1, 0)


s = Solution()
assert s.solve("dom", "mod") == 1
assert s.solve("aabc", "cbaa") == 2
assert s.solve("ysimabtyefemqebpe", "yqtempmieefyebsba") == 10