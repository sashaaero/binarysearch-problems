class Solution:
    def solve(self, n):
        odds = [1, 3, 5, 7, 9]
        s_num = [int(c) for c in str(n)]
        s_num2 = s_num[:]
        size = len(s_num)
        for i in range(size):
            if s_num[i] not in odds:
                s_num[i] += 1
                add_s = [1] * (size - (i + 1))
                s_num = s_num[:i + 1] + add_s

                if s_num2[i] != 0:
                    s_num2[i] -= 1
                    add_s = [9] * (size - (i + 1))
                    s_num2 = s_num2[:i + 1] + add_s
                    break
                else:
                    for j in range(i - 1, -1, -1):
                        if s_num2[j] > 1:
                            s_num2[j] -= 2
                            add_s = [9] * (size - (j + 1))
                            s_num2 = s_num2[:j + 1] + add_s
                            break
                    else:
                        s_num2 = [9] * (len(s_num2) - 1)

                break

        a = int(''.join([str(c) for c in s_num]))
        b = int(''.join([str(c) for c in s_num2]))
        if abs(a - n) < abs(b - n):
            return a
        return b


s = Solution()
assert s.solve(100) == 99
assert s.solve(130) == 131
assert s.solve(2222) == 1999
