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

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

