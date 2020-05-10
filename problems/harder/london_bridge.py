class Solution:
    def solve(self, G):
        time = 0
        visited = set()
        entry_time = {}
        min_time = {}
        res = 0

        def dfs(v, par=None):
            nonlocal time, res
            visited.add(v)
            entry_time[v] = time
            min_time[v] = time
            time += 1
            for to in G[v]:
                if to == par: continue
                if to in visited:
                    min_time[v] = min(min_time[v], entry_time[to])
                else:
                    dfs(to, v)
                    min_time[v] = min(min_time[v], min_time[to])
                    if min_time[to] > entry_time[v]:
                        res += 1

        for i in range(len(G)):
            if i not in visited:
                dfs(i)

        return res


s = Solution()
graph = [[1, 2, 3], [0, 5], [0, 3], [0, 2, 4], [3], [1]]
assert s.solve(graph) == 3