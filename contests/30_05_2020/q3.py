class Solution:
    def solve(self, A, k):
        mod = 10 ** 9 + 7
        r = len(A)
        c = len(A[0])
        dp = [[[-1 for _ in range(1000)] for _ in range(c)] for _ in range(r)]
        def op(i, j, k):
            if i < 0 or j < 0: return 0
            elif i == 0 and j == 0:
                return int(A[i][j] == k)
            if dp[i][j][k] != -1: return dp[i][j][k]
            dp[i][j][k] = op(i-1, j, k-A[i][j]) + op(i, j-1, k-A[i][j])
            return dp[i][j][k] % mod

        return op(r-1, c-1, k)


s = Solution()
assert s.solve([[0, 1], [1, 0]], 2) == 2
assert s.solve([[0, 0, 1],[0, 1, 1],[0, 1, 0]], 2) == 5