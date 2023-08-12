"""

Find Average value at each level of binary tree

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:

Input:

      3
     / \
    9   20
       /  \
      15   7

Output: [3, 14.5, 11]

Explanation:

The average value of nodes on level 8 is 3, on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11]."

Example 1:

Input:

      10
     / \
    8   18
       /  \
      14   20

Output: [10, 13, 17]

"""

from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def visual(self, node):
        if node is None:
            return

        print(node.value, ",", end="")

        self.visual(node.left)

        self.visual(node.right)

    def __repr__(self) -> str:
        queue = [self]

        result = []

        while len(queue):
            # will behave like queue but complexity is O(n)
            # while normal queue time complexity is O(1)
            n = queue.pop(0)

            result.append(str(n.value))

            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)

        return ", ".join(result)


class Solution(object):
    """
    BFS applied
    """

    def get_averages(self, node):
        """ """

        result = []
        queue = deque([node])

        while len(queue):

            sum = 0
            width = len(queue)

            for _ in range(width):
                n = queue.popleft()

                sum += n.value

                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)

            result.append(sum / width)

        return result


node = Node(10, Node(8), Node(18, Node(14), Node(20)))
# expected = [10, 13, 17]

node2 = Node(3, Node(9), Node(20, Node(15), Node(7)))
# expected = [3, 14.5, 11]


print(Solution().get_averages(node))
print(Solution().get_averages(node2))
