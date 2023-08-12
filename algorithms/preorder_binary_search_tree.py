# In a binary search tree, when an entry is added,
# the algorithm starts at the root node, and then moves right
# if the entry is larger than the current node or left if the entry is
# smaller than the current node. If there is no node available in the
# specified direction, the entry is added in that position.


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def _preorder_helper(self, n, ret):
        if not n:
            return
        ret += str(n.value)
        self._preorder_helper(n.left, ret)
        self._preorder_helper(n.right, ret)

    def preorder(self, n):
        ret = []
        self._preorder_helper(n, ret)
        return "".join(ret)

    def preorder_iterative(self, n):
        stack = [n]
        ret = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            ret += str(node.value)
            stack.append(node.right)
            stack.append(node.left)
        return "".join(ret)


#       1
#      / \
#     2   5
#    / \
#   3   4
n = Node(1, Node(2, Node(3), Node(4)), Node(5))
print(Solution().preorder(n))
# 12345

print(Solution().preorder_iterative(n))
# 12345
