from itertools import product

class Solution2:
    def solve(self, s):
        def p(s):
            n = len(s)
            r = []
            state = 0
            cur = ''
            i = 0
            while i < len(s):
                char = s[i]
                if char == '|':
                    r.append([cur])
                    cur = ''
                    i += 1
                elif char == '[':
                    r.append([cur])
                    cur = ''
                    end = s.find(']', i)
                    x = p(s[i + 1:end])
                    print(x)
                    y = []
                    for v in x:
                        y.append(x)
                    r.extend(y)
                    i = end + 2
                else:
                    cur += char
                    i += 1

            r.append([cur])
            return r

        if s.startswith('['):
            s = s[1:-1]

        print(p(s))
        # print(list(product(*p(s))))


class Solution:
    def solve(self, s):
        fragments = [['']]
        for c in s:
            if c == '[':
                fragments.append([''])
            elif c.isalpha():
                fragments[-1][-1] += c
            elif c == '|':
                fragments[-1].append('')
            elif c == ']':
                fragments.append([''])

        print(fragments)

s = Solution()
s.solve("cnrpv[hg|l|[y|z]]psidqyxulb")


s2 = Solution2()
s2.solve("cnrpv[hg|l|y]psidqyxulb")