# https://binarysearch.io/question/81


class Solution:
    def solve(self, matrix):
        r = len(matrix)
        c = len(matrix[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0][0] = matrix[0][0]
        max_val = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0: continue
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j - 1] + 1

                cur_w = dp[i][j]
                for k in range(i, -1, -1):
                    cur_w = min(cur_w, dp[k][j])
                    cur_h = i - k + 1
                    max_val = max(max_val, cur_h * cur_w)

        return max_val


s = Solution()
assert s.solve([[1, 0, 0, 0],[1, 0, 1, 1],[1, 0, 1, 1],[0, 1, 0, 0]]) == 4
assert s.solve([[1, 0, 0, 0, 0],[0, 0, 1, 1, 0],[0, 1, 1, 0, 0],[0, 0, 0, 0, 0],[1, 1, 0, 0, 1],[1, 1, 0, 0, 1]]) == 4
assert s.solve([[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]) == 12
assert s.solve([[1, 1, 1, 1],[1, 0, 0, 1],[1, 1, 1, 1],[1, 1, 1, 1]]) == 8