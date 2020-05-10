# https://binarysearch.io/question/139
from collections import defaultdict


class Solution:
    def solve(self, s, t):
        a = defaultdict(lambda: 1)
        b = defaultdict(lambda: 1)
        l = [0]

        if sorted(s) != sorted(t):
            return []

        for i in range(len(s)):
            a[s[i]] += (s[i] in a)
            b[t[i]] += (t[i] in b)
            if a == b and i < len(s) - 1:
                l.append(i + 1)

        return l


s = Solution()
assert s.solve("catdogwolf", "actgodflow") == [0, 2, 3, 6]
assert s.solve("study", "dusty") == [0, 4]