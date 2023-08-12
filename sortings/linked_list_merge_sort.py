import sys

sys.path.append("../")

from DataStrutures.linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce the sorted sublists until one remains

    Returns a sorted linked list

    Runs in O(kn log n)
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sub linked lists

    Takes 0 (k log n) time
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()

        mid = size // 2

        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges two linked lists, sorted by data in nodes
    Returns a new merged list

    Runs in O(n) linear time
    """

    # Create a new linked list that contains nodes from merging left and right
    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for the left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right as long until the tail node of both
    # left and right
    while left_head or right_head:
        # If the head node of left is None, we're at the tail
        # Add the tail node from right to the merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node  # Setting to None
        # If the head node of right is None, we're at the tail
        # Add the tail node from left to the merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node  # Setting to None
        else:
            # Not at either tail node
            # Perform comparison operations
            # If data on the left is less than right, set current to left node
            if left_head.data < right_head.data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on the left is larger than right, set current to right node
            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged


l = LinkedList()
l.add(20)
l.add(2)
l.add(50)
l.add(34)
l.add(23)

# print(l)
sorted_linked_list = merge_sort(l)
# print(sorted_linked_list)
