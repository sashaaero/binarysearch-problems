from collections import deque


class Solution:
    def solve(self, m):
        if not m:
            return 0
        r = len(m)
        c = len(m[0])
        ways = ((-1, 0), (1, 0), (0, 1), (0, -1))
        d = deque()
        count = 0
        for i, row in enumerate(m):
            for j, n in enumerate(row):
                if n == 2:
                    d.append((i, j))
                if n == 1:
                    count += 1
        if count == 0:
            return 0
        depth = deque()
        res = -1
        while d:
            while d:
                i, j = d.popleft()
                for x, y in ways:
                    i1, j1 = i + x, j + y
                    if 0 <= i1 < r and 0 <= j1 < c and m[i1][j1] == 1:
                        m[i1][j1] = 2
                        depth.append((i1, j1))
            d = depth
            depth = deque()
            res += 1

        return res if all(all(x != 1 for x in r) for r in m) else -1


s = Solution()
print(s.solve([[1, 1, 1],[1, 2, 1],[1, 1, 1]]))
assert s.solve([[1, 1, 1],[0, 0, 0],[1, 2, 1]]) == -1
