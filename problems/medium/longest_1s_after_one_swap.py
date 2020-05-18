class Solution:
    def solve(self, s):
        dp = [len(x) for x in s.split('0')]
        max_len = max(dp)
        a = sum(1 for x in dp if x > 0)
        if a > 2:
            for i in range(len(dp) - 2):
                max_len = max(max_len, sum(dp[i:i+2]) + 1)
        return max_len