from itertools import zip_longest


class Solution:
    def solve(self, a, b):
        ans = []
        a = map(int, reversed(a))
        b = map(int, reversed(b))
        carry = 0
        tmp = list(zip_longest(a, b, fillvalue=0))
        for i, j in tmp:
            x = i + j + carry
            if x >= 10:
                y = x - 10
                carry = 1
            else:
                y = x
                carry = 0
            ans.append(str(y))

        if carry:
            ans.append(str(carry))

        return ''.join(reversed(ans))



s = Solution()
assert s.solve("303590", "6154095") == "6457685"