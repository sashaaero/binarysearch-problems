class Solution:
    def solve(self, s):
        stack = []
        max_len = 0

        def find(l, e):
            for i, n in enumerate(l):
                if n == e:
                    return i
            return -1

        for c in s:  # avoid that stupid last char len check
            if not stack:
                stack.append(c)
                max_len = max(max_len, 1)
                continue

            i = find(stack, c)
            if i == -1:
                stack.append(c)
                max_len = max(max_len, len(stack))
                continue

            stack = stack[i+1:] + [c]

        return max_len



s = Solution()
assert s.solve("ababcde") == 5