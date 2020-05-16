from collections import deque


class Solution:
    def solve(self, m):
        r = len(m)
        c = len(m[0])

        def nei(i, j):
            if i - 1 >= 0 and m[i - 1][j] == 0: yield (i - 1, j)
            if i + 1 <= r - 1 and m[i + 1][j] == 0: yield (i + 1, j)
            if j - 1 >= 0 and m[i][j - 1] == 0: yield (i, j - 1)
            if j + 1 <= c - 1 and m[i][j + 1] == 0: yield (i, j + 1)

        seen = {(0, 0)}
        d = deque([(0, 0)])
        while d:
            i, j = d.popleft()
            if (i, j) == (r - 1, c - 1):
                return True

            for i1, j1 in nei(i, j):
                if (i1, j1) in seen: continue
                d.append((i1, j1))
                seen.add((i1, j1))

        return False


s = Solution()
assert s.solve([[0, 1, 0], [0, 0, 0], [1, 1, 0]]) == True
assert s.solve([[0, 1, 0], [1, 1, 1], [1, 1, 0]]) == False
