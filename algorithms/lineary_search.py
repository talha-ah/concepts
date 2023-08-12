def linear_search(list, target):
    """
    Returns the index of the target in the list if found, otherwise returns None
    """
    """ Time complexity
    Best Case: O(1)
    Worst Case: O(n)
    """
    """ Space comlexity
    Best Case: O(1)
    Worst Case: O(1)
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(result):
    """
    Verifies the result of the linear search
    """
    if result is not None:
        print("Target found at index", result)
    else:
        print("Target not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 5)

verify(result)
