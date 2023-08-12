class Node(object):
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        curr = self

        while curr:
            print(curr.value, end=" ")
            curr = curr.next

        return ""


class Solution(object):
    def __list_to_array(self, l):
        curr = l

        array = []

        while curr:
            array.append(curr.value)
            curr = curr.next

        return array

    def add_by_array(self, l1, l2):
        a1 = self.__list_to_array(l1)
        a2 = self.__list_to_array(l2)

        remainder = 0

        result = current = None

        for i in range(len(a1) - 1, -1, -1):
            sum = a1[i] + a2[i] + remainder

            remainder = sum // 10
            sum = sum % 10

            if not result:
                result = Node(sum)
                current = result
            else:
                current.next = Node(sum)
                current = current.next

        return result

    def add_by_lists(self, l1, l2):
        result = current = None

        remainder = 0

        while l1 or l2:
            sum = remainder

            if l1:
                sum = sum + l1.value
                l1 = l1.next
            if l2:
                sum = sum + l2.value
                l2 = l2.next

            remainder = sum // 10
            sum = sum % 10

            if not result:
                result = Node(sum)
                current = result
            else:
                current.next = Node(sum)
                current = current.next

        return result


l1 = Node(2, Node(4, Node(3)))

l2 = Node(5, Node(6, Node(4, Node(8))))

answer = Solution().add_by_array(l1, l2)
print(answer)
answer = Solution().add_by_lists(l1, l2)
print(answer)
