from helpers.classes import LLNode


class Solution:
    def solve(self, node):
        ll = []
        while node:
            ll.append(node.val)
            node = node.next

        mid = (len(ll) // 2) + (len(ll) % 2)
        i = mid - 1 - (len(ll) % 2)
        j = mid
        d = []
        if len(ll) % 2 == 1:
            d.append(ll[mid-1])
        while i >= 0:
            d.append(ll[i] + ll[j])
            i -= 1
            j += 1

        prev = root = LLNode(d[0])
        for n in d[1:]:
            new = LLNode(n)
            prev.next = new
            prev = new
        return root




s = Solution()
assert s.solve(LLNode.make('1 -> 2 -> 5 -> 8')) == LLNode.make('7 -> 9')
assert s.solve(LLNode.make('1 -> 2 -> 3 -> 4 -> 7')) == LLNode.make('3 -> 6 -> 8')
assert s.solve(LLNode.make('3 -> 1 -> 2 -> 4')) == LLNode.make('3 -> 7')
assert s.solve(LLNode.make('2 -> 5 -> 1 -> 4 -> 3')) == LLNode.make('1 -> 9 -> 5')