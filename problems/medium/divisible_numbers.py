class Solution:
    def solve(self, n, a, b, c):
        e = 1
        i = 0
        a, b, c = sorted([a, b, c])
        x = a
        y = b
        z = c

        while i < n:
            m = min(x, y, z)
            changed = False
            if x == m:
                e = x
                x += a
                changed = True
            if y == m:
                if not changed:
                    changed = True
                    e = y
                y += b
            if z == m:
                if not changed:
                    e = z
                z += c
            i += 1

        return e


s = Solution()
assert s.solve(4, 293, 383, 373) == 586
assert s.solve(8, 2, 5, 7) == 12

from datetime import datetime

start = datetime.now()
assert s.solve(87728, 157, 359, 397) == 7541154
print((datetime.now() - start).microseconds)