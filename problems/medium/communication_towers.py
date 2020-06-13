from collections import deque


class Solution:
    def solve(self, A):
        r = len(A)
        c = len(A[0])

        def nei(i, j):
            if i + 1 < r and A[i + 1][j] == 1: yield (i + 1, j)
            if j + 1 < c and A[i][j + 1] == 1: yield (i, j + 1)

        res = 0

        for i in range(r):
            for j in range(c):
                if A[i][j] == 0: continue
                res += 1
                d = deque([(i, j)])
                while d:
                    x, y = d.popleft()
                    A[x][y] = 0
                    for x1, y1 in nei(x, y):
                        d.append((x1, y1))

        return res

s = Solution()
s.solve([[0, 1, 0, 0],[1, 0, 1, 1],[0, 0, 0, 0]])