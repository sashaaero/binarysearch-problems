from collections import defaultdict


class Solution:
    def solve(self, edges):
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)


        def count(v):
            if w[v]:
                return d[v]




s = Solution()
s.solve([[0, 1],
[1, 2],
[0, 3]])



