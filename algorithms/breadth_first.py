class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BreadFirst(object):
    def __init__(self) -> None:
        pass

    def iteration(self, node):
        result = ""

        queue = [node]

        while len(queue):
            n = queue.pop(0)

            result = result + str(n.value)

            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)

        return result

    def is_binary(self, node):
        queue = [node]

        while len(queue):
            n = queue.pop(0)

            if n.left and n.right:
                queue.append(n.left)
                queue.append(n.right)
            elif n.left or n.right:
                return False

        return True

    def search(self, node, key):
        queue = [node]

        while len(queue):
            n = queue.pop(0)

            if n.value == key:
                return True

            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)

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


print(BreadFirst().iteration(tree))
print(BreadFirst().is_binary(tree))
print(BreadFirst().search(tree, 12))
