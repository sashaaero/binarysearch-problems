class Solution:
    def solve(self, n):
        arr = list(map(int, str(n)))
        last = len(arr)

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                arr[i] -= 1
                last = i + 1

        arr[last:] = [9] * (len(arr) - last)

        return int("".join(map(str, arr)))