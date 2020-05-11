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
        list_1_data = [1.0, 2.0, 3.0, 4.0, 5.0]
        list_1 = LLNode.make(' -> '.join(map(str, list_1_data)), converter=float)
        list_2 = LLNode(1.0)
        list_2.next = LLNode(2.0)
        list_2.next.next = LLNode(3.0)
        list_2.next.next.next = LLNode(4.0)
        list_2.next.next.next.next = LLNode(5.0)
        self.assertEqual(list_1, list_2)


class TestBinaryTreeBuilding(TestCase):
    def test(self):
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
        tree_1 = Tree.make(tree_dict)
        tree_2 = Tree(1)
        tree_2.left = Tree(2)
        tree_2.left.left = Tree(3)
        tree_2.left.right = Tree(4)
        tree_2.right = Tree(5)
        tree_2.right.left = Tree(6)
        tree_2.right.right = Tree(7)
        self.assertEqual(tree_1, tree_2)
