class Solution:
    def solve(self, words):
        _end = '.'
        trie = dict()
        for word in words:
            current_dict = trie
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[_end] = _end

        def dfs(char, data, turn):
            # print('player %d: char %s' % (turn, char))
            if char == '.':
                return turn == 1  # if player 1 meet the dot - he won
            return any(dfs(child, d, (2 if turn == 1 else 1)) for child, d in data.items())

        return dfs(None, trie, 2)



s = Solution()
assert s.solve(["ghost", "ghostbuster", "gas"]) == False
