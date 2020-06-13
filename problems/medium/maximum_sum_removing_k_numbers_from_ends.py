class Solution:
    def solve(self, nums, k):
        ps=[0]
        ss=[0]
        ans=0
        for n in nums:
            ps.append(ps[-1]+n)
        for i in range(len(nums)-1,-1,-1):
            ss.append(ss[-1]+nums[i])

        #ps = ps[1:]
        #ss = ss[1:]
        print(ps)
        print(ss)

        for i in range(k + 1):
            ans = max(ans, ps[i] + ss[k - i])
        return ans


class Solution2:
    def solve(self, nums, k):
        p = [nums[0]]
        for i, n in enumerate(nums):
            if i == 0: continue
            p.append(p[-1] + n)

        s = [0<nums[-1]]
        for j, n in enumerate(nums[::-1]):
            if j == 0: continue
            s.append(s[-1] + n)


        print(p, s)
        ans = 0
        for i in range(k):
            ans = max(ans, p[i] + s[k - i])
        return ans

s = Solution()
s2 = Solution2()

print(s.solve([1, 3, 4, 2, 0], 2))
print(s2.solve([1, 3, 4, 2, 0], 2))