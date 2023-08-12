class Solution(object):
    """
    Returns the index of the target in the list if found, otherwise returns None
    """

    """ Time complexity => O(ln n)
    for every amount of increase in n (say 10), the time also increase by an amount (say 1)
    """
    """ Space comlexity => O(1)
    constant space as there are just reassignments
    for a given n number of list, at the start, end and mid of the function
    there will be a constant space used by the function
    """

    def __init__(self) -> None:
        pass

    def iteratively(self, array, val):
        start = 0  # constant time
        end = len(array)  # constant time as python stores the length of the lists

        while start != end:
            # comparison is constant time
            # but while loop is the one that causes the runtime to grow

            mid = (start + end) // 2  # constant time

            if val == array[mid]:  # constant time
                return mid

            elif val > array[mid]:  # constant time
                start = mid + 1  # constant time

            else:
                end = mid  # constant time

        return -1

    def __recursive_helper(self, array, val, start, end):
        if start == end:
            return -1

        mid = (start + end) // 2

        if val == array[mid]:
            return mid

        elif val > array[mid]:
            return self.__recursive_helper(array, val, mid + 1, end)

        else:
            return self.__recursive_helper(array, val, start, mid)

    def recursive(self, array, val):
        return self.__recursive_helper(array, val, 0, len(array))

    def verify(result):
        """
        Verifies the result of the linear search
        """
        if result is not None:
            print("Target found at index", result)
        else:
            print("Target not found")


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(Solution().iteratively(array, 1))
print(Solution().iteratively(array, 2))
print(Solution().iteratively(array, 3))
print(Solution().iteratively(array, 4))
print(Solution().iteratively(array, 5))
print(Solution().iteratively(array, 6))
print(Solution().iteratively(array, 7))
print(Solution().iteratively(array, 8))
print(Solution().iteratively(array, 9))
print(Solution().iteratively(array, 10))

result = Solution().iteratively(array, 10)
verify(result)


print(Solution().recursive(array, 1))
print(Solution().recursive(array, 2))
print(Solution().recursive(array, 3))
print(Solution().recursive(array, 4))
print(Solution().recursive(array, 5))
print(Solution().recursive(array, 6))
print(Solution().recursive(array, 7))
print(Solution().recursive(array, 8))
print(Solution().recursive(array, 9))
print(Solution().recursive(array, 10))


result = Solution().recursive(array, 10)
verify(result)
