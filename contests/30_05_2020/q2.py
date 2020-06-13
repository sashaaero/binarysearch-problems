from heapq import heapify, heappop, heappush


class Solution:
    def solve(self, nums, k):
        nums = [-x for x in nums]
        heapify(nums)
        while k:
            x = heappop(nums)
            x += 1
            k -= 1
            heappush(nums, x)

        nums = [-x for x in nums]
        return max(nums)



s = Solution()
print(s.solve([2, 3, 5, 4], 6))
print(s.solve([5, 5, 5, 5], 7))