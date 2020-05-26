class Solution:
    def solve(self, nums, k):
        s = 0
        last_lo = 0
        for _ in range(k):
            max_val = -1e9
            cur_max = lo = hi = 0
            i = last_lo
            if last_lo >= len(nums) - 1:
                break
            for j in range(last_lo, len(nums)):
                cur_max += nums[j]
                if cur_max > max_val:
                    max_val = cur_max
                    lo = i
                    hi = j
                if cur_max < 0:
                    cur_max = 0
                    i = j + 1

            s += max_val
            last_lo = hi + 1

            for x in range(lo, hi + 1):
                nums[x] = -1e9

        return s


s = Solution()
res = s.solve([0, 2, 0], 3)
assert res == 2, res