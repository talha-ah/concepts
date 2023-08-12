class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def iter(self, root):
        stack = [root]

        while len(stack):
            node = stack.pop()

            if node.left and node.right:
                stack.append(node.left)
                stack.append(node.right)

            elif node.left or node.right:
                return False

        return True

    def recur(self, root):
        if not root:
            return True

        if root.left and root.right:
            return self.recur(root.left) and self.recur(root.right)

        elif root.left or root.right:
            return False

        else:
            return True


"""
                                1
                2                               3
        4               5               6               7
    8       9       10      11      12      13      14      15
"""

tree = Node(
    1,
    Node(
        2,
        Node(4, Node(8), Node(9)),
        Node(5, Node(10), Node(11)),
    ),
    Node(
        3,
        Node(6, Node(12), Node(13)),
        Node(7, Node(14), Node(15)),
    ),
)

print(Solution().iter(tree))
print(Solution().recur(tree))
