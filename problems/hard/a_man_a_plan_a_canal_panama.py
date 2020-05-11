# https://binarysearch.io/question/91


class Solution:
    def solve(self, s):
        def is_palidrome(s):
            return s == s[::-1]
        A = [[None for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            A[i][i] = True
        for i in range(len(s) - 1):
            A[i][i + 1] = s[i] == s[i + 1]

        i, k = 0, 3
        while k <= len(s):
            while i < (len(s) - k + 1):
                j = i + k - 1
                A[i][j] = A[i + 1][j - 1] and s[i] == s[j]
                i += 1
            k += 1
            i = 0

        P = [None for _ in range(len(s) + 1)]
        P[0] = []
        for i in range(len(P)):
            for j in range(i):
                matrix_i = i - 1
                if A[j][matrix_i]:
                    if P[i] is None or (len(P[j]) + 1 < len(P[i])):
                        P[i] = P[j] + [s[j:i]]
        return len(P[-1])


s = Solution()
assert s.solve("amanaplanacanalpanama") == 1
assert s.solve("racecarannakayak") == 3
assert s.solve("abc") == 3
assert s.solve("atabatab") == 2
