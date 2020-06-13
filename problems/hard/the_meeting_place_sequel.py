from collections import deque


class Solution:
    def solve(self, A):
        r = len(A)
        c = len(A[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        visited = [[0 for _ in range(c)] for _ in range(r)]

        def nei(i, j):
            if i - 1 >= 0 and A[i - 1][j] != 1: yield (i - 1, j)
            if i + 1 < r and A[i + 1][j] != 1: yield (i + 1, j)
            if j - 1 >= 0 and A[i][j - 1] != 1: yield (i, j - 1)
            if j + 1 < c and A[i][j + 1] != 1: yield (i, j + 1)

        for i in range(r):
            for j in range(c):
                if A[i][j] != 2: continue
                seen = {(i, j)}
                d = deque([(i, j, 0)])
                while d:
                    x, y, s = d.popleft()
                    dp[x][y] = max(dp[x][y], s)
                    visited[x][y] += 1
                    if s == 30: continue
                    for x1, y1 in nei(x, y):
                        if (x1, y1) not in seen:
                            seen.add((x1, y1))
                            d.append((x1, y1, s + 1))

        for row in dp:
            print(row)



s = Solution()
assert s.solve([[2, 0, 1, 0],[1, 0, 1, 2],[0, 0, 2, 2]]) == 3