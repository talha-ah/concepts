from queue import deque


class Node(object):
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

    def preorder(self):
        """
        Value - Left - Right
        """
        if not self:
            return []

        # print(self.value)
        # self.inorder(self.left)
        # self.inorder(self.right)
        return [self.value] + self.preorder[self.left] + self.preorder[self.right]

    def postorder(self):
        """
        Left - Right - Value
        """
        if not self:
            return []

        # self.inorder(self.left)
        # self.inorder(self.right)
        # print(self.value)
        return self.postorder[self.left] + [self.value] + self.postorder[self.right]

    def inorder(self):
        """
        Left - Value - Right
        """

        if not self:
            return []

        # self.inorder(self.left)
        # print(self.value)
        # self.inorder(self.right)
        return self.inorder[self.left] + self.inorder[self.right] + [self.value]

    def dfs(self):
        print(self.value, end="")
        for child in self.children:
            child.dfs()

    def dfs_iteratively(self):
        stack = [self]

        while len(stack):
            node = stack.pop()
            print(node.value, end="")
            for child in reversed(node.children):
                stack.append(child)

    def dfs_postorder(self):
        for child in self.children:
            child.dfs_postorder()
        print(self.value, end="")

    def bfs(self):
        queue = deque([self])

        while len(queue):
            node = queue.popleft()
            print(node.value, end="")
            for child in node.children:
                queue.append(child)


#       a
#     /  \
#    b    c
#   / \    \
#  d   e    f

root = Node("a", [Node("b", [Node("d"), Node("e")]), Node("c", [Node("f")])])

root.dfs()
# abdecf

print()

root.dfs_iteratively()
# abdecf

print()

root.dfs_postorder()
# debfca

print()

root.bfs()
# abcdef


class NodeLeftRight(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def preorder(self):
        # V-L-R
        stack = [self]

        while len(stack):
            node = stack.pop()

            print(node.value, end="")

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    def inorder(self):
        stack = []
        current = self

        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.value, end="")

                current = current.right
            else:
                break

    def postorder(self):
        stack = []
        current = self

        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.value, end="")

                current = current.right
            else:
                break


root = NodeLeftRight(1, None, NodeLeftRight(2, NodeLeftRight(3)))

root.preorder()
print()
root.postorder()
print()
root.inorder()
print()
