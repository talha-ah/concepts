class Node(object):
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self) -> None:
        pass

    def iteration(self, node):
        result = ""

        stack = [node]

        while len(stack):
            n = stack.pop()

            result = result + str(n.value)

            if n.right:
                stack.append(n.right)

            if n.left:
                stack.append(n.left)

        return result

    def is_binary(self, node):
        stack = [node]

        while len(stack):
            n = stack.pop()

            if n.left and n.right:
                stack.append(n.left)
                stack.append(n.right)
            elif n.left or n.right:
                return False

        return True

    def search(self, node, key):
        stack = [node]

        while len(stack):
            n = stack.pop()

            if n.value == key:
                return True

            if n.right:
                stack.append(n.right)

            if n.left:
                stack.append(n.left)

        return False


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

print(Solution().iteration(tree))
print(Solution().is_binary(tree))
print(Solution().search(tree, 15))
