class Solution:
    def solve(self, A, k):
        i = 0

        def find_that_shitty_index():
            return max([(A[i] - A[i - 1], i) for i in range(1, len(A))])

        while i < k:
            idx = find_that_shitty_index()[1]
            A = A[:idx] + A[idx + 1:]
            print(A)
            i += 1

        return find_that_shitty_index()[0]


s = Solution()
s.solve([76, 88, 128, 183, 192, 205, 237, 322, 502, 545, 554, 634, 690, 750, 847, 1012], 5)