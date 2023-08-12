class Solution(object):
    def first_duplicate_bruteforce(self, array):
        """
        T = O(n^2)
        """

        min_index = len(array)

        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] == array[j]:
                    min_index = min(min_index, j)

        return array[min_index] if min_index != len(array) else -1

    def first_duplicate_hashmap(self, array):
        """
        T = O(n)
        S = O(n)
        """

        hashmap = {}

        for i in range(len(array)):
            if array[i] in hashmap.keys():
                return array[i]
            else:
                hashmap[array[i]] = 1

        return -1

    def first_duplicate_negation(self, array):
        """
        T = O(n)
        """

        for i in range(len(array)):
            j = array[i]
            if array[j - 1] == -1:
                return array[i]
            else:
                array[i - 1] = -1

        return -1


input = [2, 1, 3, 5, 3, 2]

print(Solution().first_duplicate_bruteforce(input))
print(Solution().first_duplicate_hashmap(input))
print(Solution().first_duplicate_negation(input))
