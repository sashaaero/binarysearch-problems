class Solution:
    def solve(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        def sum_around(i, j):
            s = 0
            if i - 1 >= 0: s += matrix[i - 1][j]
            if i + 1 <= r - 1: s += matrix[i + 1][j]
            if j - 1 >= 0: s += matrix[i][j - 1]
            if j + 1 <= c - 1: s += matrix[i][j + 1]
            return s

        return sum(4 - sum_around(i, j) for i in range(r) for j in range(c) if matrix[i][j] == 1)


s = Solution()
s.solve([[0, 1, 1],[0, 1, 0]])