
def longest_palindrome(s):
    n = len(s)
    dp = [[0 for x in range(n)] for y in range(n)]
    max_len = 1
    i = 0
    while i < n:
        dp[i][i] = True
        i += 1
    start = 0
    i = 0
    while i < n - 1:
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
        i += 1

    k = 3
    while k <= n:
        i = 0
        while i < (n - k + 1):
            j = i + k - 1
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                if k > max_len:
                    start = i
                    max_len = k
            i += 1
        k += 1
    return max_len
