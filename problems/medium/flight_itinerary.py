class Solution:
    def solve(self, s):
        trips = {}
        stop = set()
        for a, b in s:
            trips[a] = b
            stop.add(b)
        origin = None
        for k in trips:
            if k not in stop:
                origin = k
                break
        res = [origin]
        while len(res) < len(stop) + 1:
            res.append(trips[res[-1]])
        return res


s = Solution()
assert s.solve([["WRE", "RPM"],["AGN", "WRE"],["NTL", "AGN"]]) == ["NTL", "AGN", "WRE", "RPM"]