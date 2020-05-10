# https://binarysearch.io/question/14
from collections import defaultdict


class Solution:
    def solve(self, k, s):
        counter = defaultdict(int)
        start = end = 0
        max_window_size = 1
        counter[s[0]] += 1

        uniques = 1
        for i in range(1, len(s)):
            if counter[s[i]] == 0:
                uniques += 1
            counter[s[i]] += 1
            end += 1
            while uniques > k:
                counter[s[start]] -= 1
                if counter[s[start]] == 0:
                    uniques -= 1
                start += 1
            max_window_size = max(max_window_size, end - start + 1)

        return max_window_size

s = Solution()
assert s.solve(2, "abcba") == 3
assert s.solve(1, "aaaaa") == 5
assert s.solve(1, "abcde") == 1