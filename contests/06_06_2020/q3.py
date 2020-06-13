class Solution:
    def solve(self, A, k):
        n = len(A)
        odds = [v % 2 for v in A]
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if A[j] < A[i] and dp[j] + 1 >= dp[i]:
                    odds[i] = max(odds[i], odds[j] + (A[j] % 2))
                    dp[i] = dp[j] + 1

        print(dp)
        print(odds)
        max_len = 0
        for i in range(n):
            if dp[i] > max_len and odds[i] >= k:
                max_len = dp[i]

        return max_len


s = Solution()
# 3 1 2 15

#print(s.solve([10, 12, 14, 3, 5, 6], 2))
#print(s.solve([3], 0))
#print(s.solve([4, 5], 1))
print(s.solve([50, 19, 12, 47, 5, 68, 92,
                83, 37, 8, 39, 70, 10, 45,
                17, 27, 7, 94, 3, 44, 15, 90,
                4, 36, 76, 57, 18, 63, 61, 24,
                33, 73, 23, 35, 88, 95, 2, 75,
                30, 31, 97, 42, 84, 79, 86, 67,
                66, 20, 1, 46, 85, 81, 0, 77, 40,
                51, 71, 54, 91, 9, 43, 58, 82,
                93, 6, 49, 78, 14, 60, 26, 59,
                99, 41, 52, 29, 98, 96, 32, 89,
                69, 55, 25, 22, 64, 87, 74, 21,
                28, 13, 80, 16, 38, 53, 56, 11,
                48, 65, 62, 72, 34], 10))