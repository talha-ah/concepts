import random


# Bogosort just randomly rearranges the list of values over and over,
# so the first thing it's going to need is a function to detect when
# the list is sorted. We'll write an is_sorted function that takes a
# list of values as a parameter. It will return True if the list
# passed in is sorted, or False if it isn't.


def bogo_sort(list):
    attemps = 0
    while not is_sorted(list):
        print(attemps)
        random.shuffle(list)
        attemps += 1
    return list


def is_sorted(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True


result = bogo_sort([3, 10, 2, 5, 7, 54])

print(result)
