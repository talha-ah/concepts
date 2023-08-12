class Node(object):
    """
    An object for storing a single node in a linked list

    Attributes:
        data: Data stored in node
        next: Reference to next node in linked list
    """

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList(object):
    """
    Linear data structure that stores values in nodes. The list maintains a reference to the first node, also called head. Each node points to the next node in the list

    Attributes:
        head: The head node of the list
    """

    def __init__(self):
        self.count = 0
        self.head = None

    def __increment_count(self):
        self.count += 1

    def __decrement_count(self):
        self.count -= 1

    def __repr__(self):
        current = self.head

        result = []
        while current:
            result.append(str(current.value))
            current = current.next

        return (" -> ").join(result) or "empty"

    def is_empty(self):
        """
        Determines if the linked list is empty
        Takes O(1) time
        """

        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) linear time
        """

        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next

        return count

    def node_index(self, data: any):
        current = self.head
        index = -1
        position = 0

        while current and index == -1:
            if current.data == data:
                index = position
            else:
                current = current.next
                position += 1

        return index

    def node_at_index(self, index):
        """
        Returns the Node at specified index
        T = O(n)
        """

        if index + 1 > self.count:
            return None

        if index == 0:
            return self.head

        position = 0
        current = self.head

        while position < index:
            current = current.next
            position += 1

        return current

    def add_at_head(self, data):
        """
        Add a new node containing data at the head of the list
        Also called prepend
        Takes O(1) constant time which is our best case scenario
        """

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.__increment_count()

    def add_at_tail(self, value):
        """
        Add a new node containing data at the tail of the list
        Also called append
        Takes O(n) constant time which is our best case scenario
        """

        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node

        self.__increment_count()

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding node at insertion point takes
        O(n) time.
        T = O(n)
        """

        if index == 0:
            return self.add_at_head(data)

        if index == self.count:
            return self.add_at_tail(data)

        if index + 1 > self.count:
            raise Exception("Sorry, index not found")

        if index > 0:
            new_node = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next
                position -= 1

            new_node.next = current.next
            current.next = new_node

        self.__increment_count()

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or None if key doesn't exist
        T = O(n)
        """

        self.__decrement_count()

        current = self.head

        if current.data == key:
            self.head = current.next
            current.next = None
            return current

        found = False
        previous = None

        while current and not found:
            if current.data == key:
                previous.next = current.next
                current.next = None
                found = True
            else:
                previous = current
                current = current.next

        return current

    def remove_at_index(self, index):
        """
        Removes Node at specified index
        T = O(n)
        """

        self.__decrement_count()

        current = self.head

        if index + 1 > self.count:
            raise Exception("Sorry, index not found")

        if index == 0:
            self.head = current.next
            current.next = None
            return current

        previous = None
        position = index

        while current and position > 0:
            previous = current
            current = current.next
            position -= 1

        previous.next = current.next

        return current

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or `None` if not found
        T = O(n)
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next

        return None

    def reverse(self):
        """
        Time complexity O(n)
        Space complexity O(1)
        """
        reverse_ll = None  # constant
        current = self.head  # constant

        while current:  # linear
            new_node = Node(current)  # constant

            if not reverse_ll:  # constant
                reverse_ll = new_node  # constant
            else:  # constant
                new_node.next = reverse_ll  # constant
                reverse_ll = new_node  # constant

            current = current.next  # constant

        self.head = reverse_ll  # constant
        return self  # constant

    def oddEven(self):
        """
        Considering the node number, not index, not value

        Input: 1->2->3->4->5->NULL
        Output: 1->3->5->2->4->NULL

        Input: 2->1->3->5->6->4->7->NULL
        Output: 2->3->6->7->1->5->4->NULL

        The program should run in O(1) space complexity and O(nodes) time complexity
        """

        if not self.head or not self.head.next:
            return self.head

        even_head = self.head.next
        even = self.head.next
        odd = self.head

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = even_head
        return self

    def palindrome(self):
        """
        Could you do it in O(n) time and O(1) space
        """

        simple = []
        current = self.head

        while current:
            simple.append(current.value)
            current = current.next

        j = len(simple) - 1

        for i in range(0, len(simple)):
            if simple[i] != simple[len(simple) - (i + 1)]:
                return False
            j -= 1

        return True


# result = l.search(5)
# result = l.remove(5)


ll = LinkedList()
ll.add_at_tail(1)
ll.add_at_tail(2)
ll.add_at_tail(3)
ll.add_at_tail(3)
ll.add_at_tail(2)
ll.add_at_tail(1)
ll.insert(5, 3)
ll.remove_at_index(5)
print(ll.node_at_index(5))
print(ll)
print(ll.palindrome())
