# https://binarysearch.io/question/306

class Solution:
    def solve(self, a, b, c):
        x, y, z = len(a), len(b), len(c)
        dp = [[[0 for _ in range(z + 1)] for _ in range(y + 1)] for _ in range(x + 1)]
        for i in range(x + 1):
            for j in range(y + 1):
                for k in range(z + 1):
                    if 0 in (i, j, k):
                        dp[i][j][k] = 0
                    elif a[i - 1] == b[j - 1] == c[k - 1]:
                        dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                    else:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

        return dp[-1][-1][-1]


s = Solution()
assert s.solve("epidemiologist", "refrigeration", "supercalifragilisticexpialodocious") == 5