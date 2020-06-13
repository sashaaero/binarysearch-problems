def lev(a, b):
    n = len(a) + 1
    m = len(b) + 1
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = i
    for j in range(m):
        dp[0][j] = j

    for i in range(1, n):
        for j in range(1, m):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j] + 1,
                    dp[i-1][j-1] + 1,
                    dp[i][j-1] + 1
                )

    return dp[-1][-1]

