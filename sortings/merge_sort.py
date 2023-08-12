def merge_sort_2(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left_part = merge_sort_2(list[:mid])
    right_part = merge_sort_2(list[mid:])

    print("%15s %-15s" % (left_part, right_part))

    sorted_values = []
    left_index = 0
    right_index = 0

    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] < right_part[right_index]:
            sorted_values.append(left_part[left_index])
            left_index += 1
        else:
            sorted_values.append(right_part[right_index])
            right_index += 1

    sorted_values += left_part[left_index:]
    sorted_values += right_part[right_index:]

    return sorted_values


def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the endpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes overall O(n log n) time
    Takes linear space O(n) times
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublits - left and right

    Takes overall O(k log n) time
    In turn, the overall time of merge sort will be O(kn log n)
    """

    # mid = len(list) // 2

    # left = list[:mid]  # not a constant time, split takes O(k) where k is the slice time (from python documentation)
    # right = list[mid:] # not a constant time depends on the language

    """
    Second apporach to split manually
    
    Takes overall O(log n) time
    """

    left = []
    right = []

    start = 0
    end = len(list) // 2

    while start < end:
        left.append(list[start])
        start += 1

    start = end
    end = len(list)

    while start < end:
        right.append(list[start])
        start += 1

    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def is_sorted(list):
    n = len(list)

    if n <= 1:
        return True

    return list[0] <= list[1] and is_sorted(list[1:])


numbers = [5, 4, 6, 2, 6, 6, 56, 34, 3]

result = merge_sort(numbers)
result = merge_sort_2(numbers)

print(is_sorted(result))
