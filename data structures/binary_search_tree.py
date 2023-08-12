class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        stack = [self]

        while len(stack):
            node = stack.pop()

            print(node.value, end=" ")

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ""


class Methods(object):
    def __init__(self):
        pass

    def check(self, root):
        stack = [root]

        while len(stack):
            node = stack.pop()

            if node.left and node.right:
                stack.append(node.left)
                stack.append(node.right)

            elif node.left or node.right:
                return False

        return True

    def search(self, root, val):
        stack = [root]

        while len(stack):
            node = stack.pop()

            if node.value == val:
                return True

            elif node.value > val:
                if node.left:
                    stack.append(node.left)

            else:
                if node.right:
                    stack.append(node.right)

        return False

    def insert(self, root, val):
        stack = [root]

        while len(stack):
            node = stack.pop()

            if node.value >= val:
                if node.left:
                    stack.append(node.left)
                else:
                    node.left = Node(val)
                    return
            else:
                if node.right:
                    stack.append(node.right)
                else:
                    node.right = Node(val)
                    return

        return

    def height(self, root):
        result = 0

        stack = [root]

        while len(stack):
            node = stack.pop()

            result = result + 1

            if node.left:
                stack.append(node.left)

        return result

    def height_rec(self, root):
        if root.left:
            return 1 + self.height(root.left)
        else:
            return 0


"""
                                15
                    14                      16
            12                          16          18
        11                                                  19
                                                                     25
                                                                20
"""

tree = Node(15)

Methods().insert(tree, 16)
Methods().insert(tree, 14)
Methods().insert(tree, 12)
Methods().insert(tree, 18)
Methods().insert(tree, 19)
Methods().insert(tree, 25)
Methods().insert(tree, 20)
Methods().insert(tree, 16)
Methods().insert(tree, 11)

print(tree)
print(Methods().height(tree))
print(Methods().height_rec(tree))
