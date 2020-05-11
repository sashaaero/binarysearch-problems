# https://binarysearch.io/question/366
from helpers.classes import Tree, val, left, right


class Solution:
    def solve(self, root, lo, hi):
        def op(node):
            if node is None: return
            if node.val < lo:
                return op(node.right)

            if node.val > hi:
                return op(node.left)

            node.left = op(node.left)
            node.right = op(node.right)
            return node

        return op(root)


s = Solution()
tree = Tree.make({val: 2, left: {val: 1, left: {val: 0, left: None, right: None}, right: None}, right: {val: 4, left: {val: 3, left: None, right: None}, right: None}})
tree2 = Tree.make({val: 4, left: {val: 3, left: None, right: None}, right: None})
assert s.solve(tree, 3, 4) == tree2