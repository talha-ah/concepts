# Quicksort works by picking a pivot value, then splitting the full list into two sub-lists.
# The first sub-list has all the values less than or equal to the pivot, and the second
# sub-list has all the values greater than the pivot. The quicksort function recursively
# calls itself to sort these sublists, and then to sort the sublists of those sub-lists,
# until the full list is sorted


def quicksort(list):
    if len(list) <= 1:
        return list

    less_than_pivot = []
    greater_than_pivot = []
    pivot = list[0]

    for i in list[1:]:
        if i <= pivot:
            less_than_pivot.append(i)
        else:
            greater_than_pivot.append(i)

    print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


def is_sorted(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True


print(quicksort([3, 10, 2, 5, 7, 54]))
