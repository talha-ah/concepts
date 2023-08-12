class Node(object):
    """
    object here is the type of the structure
    """

    def __init__(self, value, previous=None, next=None):
        self.previous = previous
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)


class DoublyLinkedList(object):
    def __init__(self):
        self.count = 0
        self.head = 0

    def __increment_count(self):
        self.count += 1

    def __decrement_count(self):
        self.count -= 1

    def get(self, index):
        if index + 1 > self.count:
            raise Exception("Sorry, index out of range")

        if index == 0:
            return self.head

        current = self.head
        position = index

        while current and position > 0:
            current = current.next
            position += 1

        return current

    def add_at_head(self, value):
        """ """

        self.__increment_count()

        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return new_node

        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

        return new_node

    def add_at_tail(self, value):
        """ """

        self.__increment_count()

        if not self.head:
            new_node = Node(value)
            self.head = new_node
            return new_node

        current = self.head

        while current.next:
            current = current.next

        new_node = Node(value)
        current.next = new_node
        new_node.previous = current

        return new_node

    def add_at_index(self, value, index):
        """ """

        if index == 0:
            return self.add_at_head(value)

        if index == self.count:
            return self.add_at_tail(value)

        if index + 1 > self.count:
            raise Exception("Sorry, index out of range")

        current = self.head
        position = index

        while current and position > 0:
            current = current.next
            position -= 1

        new_node = Node(value)

        previous = current.previous

        new_node.next = current
        new_node.previous = previous

        current.previous = new_node
        previous.next = new_node

        self.__increment_count()

        return new_node

    def delete_at_index(self, index):
        """ """

        if index + 1 > self.count:
            raise Exception("Sorry, index out of range")

        self.__decrement_count()

        if index == 0:
            current = self.head
            self.head.next.previous = None
            self.head = self.head.next
            return current

        current = self.head
        position = index

        while current and position > 0:
            current = current.next
            position -= 1

        next = current.next
        previous = current.previous

        previous.next = next
        next.previous = current.previous

        return current

    def __repr__(self):
        current = self.head

        result = []
        result_detailed = []
        while current:
            result.append(str(current.value))
            result_detailed.append(
                f"{current.previous} <- {current.value} -> {current.next}"
            )

            current = current.next

        result = (" -> ").join(result)
        result_detailed = (" :: ").join(result_detailed)

        return result + "\n" + result_detailed or "empty"


dll = DoublyLinkedList()
dll.add_at_tail(10)
dll.add_at_tail(11)
dll.add_at_tail(12)
dll.add_at_head(8)
dll.get(0)
dll.add_at_index(7, 0)
dll.add_at_index(9, 2)
dll.add_at_index(13, 6)
dll.add_at_index(15, 7)
print(dll)
dll.delete_at_index(2)
print(dll)
