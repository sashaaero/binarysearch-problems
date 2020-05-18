class Solution:
    def solve(self, nums):
        def op(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-8
            for i in range(len(nums) - 1):
                x = nums[i]
                y = nums[i + 1]
                vals = [x + y, x * y, x - y]
                if y:
                    vals.append(x / y)
                B = nums[:]
                B.pop(i)
                for z in vals:
                    B[i] = z
                    if op(B): return True
            return False
        return op(nums)