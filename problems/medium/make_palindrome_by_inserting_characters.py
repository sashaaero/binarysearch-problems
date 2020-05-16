class Solution:
    def solve(self, s):
        size = len(s)
        dp = [[0 for _ in range(size)] for _ in range(size)]
        for k in range(1, size):
            i = 0
            for j in range(k, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
                i += 1

        return dp[0][-1]


s = Solution()
print(s.solve("qwblxznzeuqpzgucwnaoyptskczsynilsoqqvohvtrscvoybwix"))
