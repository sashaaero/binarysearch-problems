class Solution:
    def solve(self, intervals):
        intervals.sort()
        stack = []
        for a, b in intervals:
            if stack and a <= stack[-1][1]:
                stack[-1][1] = max(b, stack[-1][1])
            else:
                stack.append([a,b])

        return stack

s = Solution()
assert s.solve([[0, 5],[4, 6]]) == [[0,6]]