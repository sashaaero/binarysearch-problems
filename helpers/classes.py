class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    @classmethod
    def make(cls, data, converter=int):
        if not data:
            return None

        data = data.replace(' ', '')
        nodes = data.split('->')
        if converter:
            nodes = list(map(converter, nodes))
        root = prev_node = LLNode(nodes[0])
        for i in range(1, len(nodes)):
            node = LLNode(nodes[i])
            prev_node.next = node
            prev_node = node
        return root

    def flat(self):
        res = []
        node = self
        while node:
            res.append(node.val)
            node = node.next
        return res

    def __eq__(self, other):
        return self.flat() == other.flat()


val = 'val'
left = 'left'
right = 'right'


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def make(cls, data):
        def parse_tree(data):
            if not data:
                return None
            return Tree(data[val], parse_tree(data.get(left)), parse_tree(data.get(right)))
        return parse_tree(data)

    def preorder(self):
        data = []
        def inner(node):
            if node is None: return
            data.append(node.val)
            inner(node.left)
            inner(node.right)

        inner(self)
        return data

    def __eq__(self, other):
        return self.preorder() == other.preorder()


