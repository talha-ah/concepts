from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        stack = [self]

        while len(stack):
            node = stack.pop(0)

            print(node.value, end=" ")

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return ""


class Methods(object):
    def __init__(self) -> None:
        pass

    def bfs(self, root):

        queue = deque([root])

        while len(queue):
            node = queue.popleft()

            print(node.value, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs(self, root):

        stack = [root]

        while len(stack):
            node = stack.pop()

            print(node.value, end=" ")

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def preorder(self, root):
        if root.left:
            self.preorder(root.left)

        print(root.value, end=" ")

        if root.right:
            self.preorder(root.right)

    def inorder(self, root):
        print(root.value, end=" ")

        if root.left:
            self.inorder(root.left)
        if root.right:
            self.inorder(root.right)

    def postorder(self, root):
        if root.left:
            self.postorder(root.left)
        if root.right:
            self.postorder(root.right)

        print(root.value, end=" ")

    def search(self, root, val):
        stack = [root]

        while len(stack):
            node = stack.pop()

            if node.value == val:
                return True

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False

    def insert(self, root, val):
        stack = [root]

        while len(stack):
            node = stack.pop()

            if node.left and node.right:
                stack.append(node.left)
                stack.append(node.right)

            elif node.left:
                node.right = Node(val)
                return

            else:
                node.left = Node(val)
                return

        return

    def is_binary(self, root):
        stack = [root]

        while len(stack):
            node = stack.pop()

            if node.left and node.right:
                stack.append(node.left)
                stack.append(node.right)
            elif node.left or node.right:
                return False

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


print(tree)
