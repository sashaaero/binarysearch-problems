# https://binarysearch.io/question/58


class Solution:
    def solve(self, s):
        size = len(s)
        dp = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(len(s)):
            dp[i][i] = 1  # all palindromes of length 1

        for l in range(2, size + 1):  # all lengths
            for i in range(size - l + 1):  # start
                j = i + l - 1  # end
                if s[i] == s[j]:
                    if l == 2:
                        dp[i][j] = 2  # palindrome of len 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2  # we're adding 2 characters
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])  # skip this char

        return dp[0][-1]


s = Solution()
assert s.solve("rbaicneacrayr") == 7
assert s.solve("binarysearch") == 3
assert s.solve("bbbbbbbbbb") == 10
assert s.solve("a") == 1

