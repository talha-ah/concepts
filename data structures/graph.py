from collections import deque


class Node(object):
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children


class Methods(object):
    def __init__(self) -> None:
        pass

    def dfs(self, root):
        stack = [root]

        while len(stack):
            node = stack.pop()

            print(node.value, end=" ")

            for child in reversed(node.children):
                stack.append(child)

    def bfs(self, root):
        stack = deque([root])

        while len(stack):
            node = stack.popleft()

            print(node.value, end=" ")

            for child in node.children:
                stack.append(child)

    def pre_order(self, root):
        stack = [root]

        while len(stack):
            node = stack.pop()

            print(node.value, end=" ")

            for child in reversed(node.children):
                stack.append(child)

    def post_order(self, root):
        for child in root.children:
            self.post_order(child)

        print(root.value, end=" ")


"""
                                1
                2                               3
        4               5               6               7
    8       9       10      11      12      13      14      15
"""

graph = Node(
    1,
    [
        Node(
            2,
            [
                Node(
                    4,
                    [Node(8), Node(9)],
                ),
                Node(
                    5,
                    [Node(10), Node(11)],
                ),
            ],
        ),
        Node(
            3,
            [
                Node(
                    6,
                    [Node(12), Node(13)],
                ),
                Node(
                    7,
                    [Node(14), Node(15)],
                ),
            ],
        ),
    ],
)


Methods().dfs(graph)
print("")
Methods().bfs(graph)
print("")
Methods().pre_order(graph)  # 1 2 4 8 9 5 10 11 3 6 12 13 7 14 15
print("")
Methods().post_order(graph)  # 8 9 4 10 11 5 2 12 13 6 14 15 7 3 1
# Methods().in_order(graph)  # difficult as there can a number of children
