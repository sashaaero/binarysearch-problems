from collections import defaultdict, deque

class Solution:
    def solve(self, s, d, p):
        g = defaultdict(list)
        for a, b in zip(s, d):
            g[a].append(b)
            g[b].append(a)

        a = b = 0
        def dfs(node, par, c):
            nonlocal a, b
            if c:
                a += p[node]
            else:
                b += p[node]

            for n in g[node]:
                if n != par:
                    dfs(n, node, not c)

        dfs(0, None, False)
        return max(a, b)


s = Solution()
assert s.solve([0, 0, 2, 2], [1, 2, 4, 3], [5, 7, 3, 2, 4]) == 11