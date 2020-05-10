# https://binarysearch.io/question/59


class Solution:
    def solve(self, str1, str2):
        r = len(str1) + 1
        c = len(str2) + 1
        dp = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if 0 in (i, j):
                    dp[i][j] = 0
                elif str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


s = Solution()
assert s.solve("abcvc", "bv") == 2
assert s.solve("abc", "abc") == 3
assert s.solve("abc", "def") == 0
assert s.solve("binarysearch", "searchbinary") == 6
