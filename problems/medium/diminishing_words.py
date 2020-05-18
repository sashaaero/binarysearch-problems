class Solution:
    def solve(self, words, s):
        words = set(words)
        def removal(word):
            s = len(word)
            res = []
            for i in range(1, s+1):
                r = word[:i-1] + word[i:]
                if r in words:
                    res.append(r)
            return res

        def dfs(word, cur_len):
            candidates = removal(word)
            if len(candidates) == 0:
                return cur_len
            return max(dfs(w, cur_len+1) for w in candidates)

        return dfs(s, 0) + (s in words)


s = Solution()
assert s.solve(["pies", "prices", "pries", "prying", "coffee", "mug", "pool", "type"], "prices") == 3
assert s.solve(["pie", "pies", "princes", "princess", "prices", "pries", "prying", "coffee", "mug", "pool", "type", "cafffe", "cofee"], "pies") == 2