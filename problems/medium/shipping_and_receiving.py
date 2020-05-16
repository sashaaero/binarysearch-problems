class Solution:
    def solve(self, ports, shipments):
        size = len(ports)
        dp = [[1e9 if i != j else 0 for j in range(size)] for i in range(size)]
        for i, vec in enumerate(ports):
            for p in vec:
                dp[i][p] = 1

        for k in range(size):
            for i in range(size):
                for j in range(size):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        s = 0
        for a, b in shipments:
            if dp[a][b] != 1e9:
                s += dp[a][b]

        return s