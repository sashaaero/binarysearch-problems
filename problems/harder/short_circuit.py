# https://binarysearch.io/question/184
from collections import deque, defaultdict


class Solution:
    def solve(self, words):
        data = []
        ends = defaultdict(lambda: 1)
        starts = defaultdict(lambda: 1)
        data = defaultdict(list)
        init = words[0][0]

        for w in words:
            a, b = w[0], w[-1]
            data[a].append(b)
            starts[a] += 1
            ends[b] += 1

        seen = set()

        def dfs(node):
            seen.add(node)
            for n in data[node]:
                if n not in seen:
                    dfs(n)

        dfs(init)
        for n in data:
            if n not in seen or starts[n] != ends[n]:
                return False

        return True


s = Solution()
assert s.solve(["chair", "height", "racket", "touch", "tunic"])

