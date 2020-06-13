class Solution:
    def solve(self, s, k):
        s = list(s)
        k -= 1
        n = len(s)
        for i in range(n):
            if s[i] == 'x': continue
            for j in range(i - k, i + k + 1):
                if not 0 <= j <= n-1: continue
                if s[j] == 'x': break
            else:
                return True

        return False



s = Solution()

assert s.solve("x..", 2) == True
assert s.solve("x..x", 2) == False