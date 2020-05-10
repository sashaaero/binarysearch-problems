from unittest import TestCase
from helpers.classes import *


class TestLinkedListBuilding(TestCase):
    def test_default_ll(self):
        list_1 = [1, 2, 3, 4, 5]
        node = LLNode.make(' -> '.join(map(str, list_1)))
        list_2 = []
        while node:
            list_2.append(node.val)
            node = node.next

        self.assertEqual(list_1, list_2)

    def test_float_ll(self):
        list_1 = [1.0, 2.0, 3.0, 4.0, 5.0]
        node = LLNode.make(' -> '.join(map(str, list_1)), converter=float)
        list_2 = []
        while node:
            list_2.append(node.val)
            node = node.next

        self.assertEqual(list_1, list_2)


class TestBinaryTreeBuilding(TestCase):
    def test(self):
        tree_1 = [1, 2, 3, 4, 5, 6, 7]
        tree_dict = {
            val: 1,
            left: {
                val: 2,
                left: {val: 3, left: None, right: None},
                right: {val: 4, left: None, right: None}
            },
            right: {
                val: 5,
                left: {val: 6, left: None, right: None},
                right: {val: 7, left: None, right: None}
            }
        }
        root = Tree.make(tree_dict)

        def preorder(tree):
            data = []

            def inner(node):
                if node is None: return
                data.append(node.val)
                inner(node.left)
                inner(node.right)
            inner(tree)
            return data

        tree_2 = preorder(root)
        self.assertEqual(tree_1, tree_2)
