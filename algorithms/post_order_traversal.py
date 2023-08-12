class Node(object):
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self) -> str:
        pass

    def traversal(self, node):
        if node:
            self.traversal(node.left)
            self.traversal(node.right)
            print(node.value)


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
        Node(
            4,
            Node(8),
            Node(9),
        ),
        Node(5, Node(10), Node(11)),
    ),
    Node(
        3,
        Node(6, Node(12), Node(13)),
        Node(7, Node(14), Node(15)),
    ),
)

Solution().traversal(tree)
