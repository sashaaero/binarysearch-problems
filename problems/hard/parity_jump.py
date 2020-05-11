from collections import deque


class Solution:
    def solve(self, nums):
        size = len(nums)
        r = []
        for i, n in enumerate(nums):
            parity = n % 2
            d = deque([(i + n, 1), (i - n, 1)])
            seen = {i + n, i - n}
            while d:
                idx, step = d.popleft()
                if not 0 <= idx < size: continue
                num = nums[idx]
                if num % 2 != parity:
                    r.append(step)
                    break
                if idx + num not in seen:
                    d.append((idx + num, step + 1))
                    seen.add(idx + num)
                if idx - num not in seen:
                    d.append((idx - num, step + 1))
                    seen.add(idx - num)
            else:
                r.append(-1)

        return r


s = Solution()
assert s.solve([5, 1, 2, 3, 4, 7, 4, 5]) == [-1, 1, 1, 1, 1, -1, 2, 1]