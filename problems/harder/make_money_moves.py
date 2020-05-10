# https://binarysearch.io/question/108


class Solution:
    def solve(self, M):
        n = len(M)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    M[i][j] = max(M[i][j], M[i][k] * M[k][j])

        for i in range(n):
            if M[i][i] > 1:
                return True

        return False


s = Solution()
assert s.solve([[1, 1.32, 0.9],[0.76, 1, 0.72],[1.11, 1.47, 1]])
assert not s.solve([[1, 0.726, 0.6139],[1.3773, 1, 0.8456],[1.6287, 1.1825, 1]])