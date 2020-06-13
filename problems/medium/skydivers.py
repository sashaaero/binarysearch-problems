class Solution:
    def solve(self, nums, k):
        if len(nums) == 1: return nums[0]
        lo = 0
        hi = sum(nums)
        while lo < hi:
            mid = ((hi - lo) // 2) + lo
            max_groups = 0
            cur_group = 0
            for n in nums:
                if cur_group + n <= mid:
                    cur_group += n
                elif n <= mid:
                    max_groups += 1
                    cur_group = n
                else:
                    lo = mid + 1
                    break
            else:
                if cur_group > 0:
                    max_groups += 1

                if max_groups <= k:
                    hi = mid
                else:
                    lo = mid + 1

        return lo if lo > 0 else max(nums)
