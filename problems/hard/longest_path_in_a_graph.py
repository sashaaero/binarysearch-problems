class Solution:
    def solve(self, graph):
        seen = {}

        def dfs(i):
            if i not in seen:
                cur = 0
                for p in graph[i]:
                    cur = max(cur, dfs(p) + 1)
                seen[i] = cur
            return seen[i]

        max_val = 0
        for i in range(len(graph)):
            max_val = max(max_val, dfs(i))
        return max_val

