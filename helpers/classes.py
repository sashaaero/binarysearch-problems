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


