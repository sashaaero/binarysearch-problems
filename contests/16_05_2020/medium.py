from math import gcd
from collections import deque


class Solution:
    def solve(self, a, b):
        d = deque([(a, b, 0)])
        seen = set()
        while d:
            x, y, s = d.popleft()
            if (x,y) in seen: continue
            seen.add((x, y))
            if gcd(x, y) != 1:
                print(s)
                return s

            d.append((x + 1, y, s + 1))
            d.append((x - 1, y, s + 1))
            d.append((x, y + 1, s + 1))
            d.append((x, y - 1, s + 1))


s = Solution()
assert s.solve(7, 23) == 2