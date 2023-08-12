class Solution(object):
    def ievs_bruteforce(self, input):
        """
        T = O(n)
        S = O(1)
        """

        for i in range(len(input)):
            if i == input[i]:
                return i

        return -1

    def ievs_binary_search(self, input):
        """
        T = O(lg n)
        S = O(1)
        """

        first = 0
        last = len(input) - 1
        smallest_index = len(input)

        while first <= last:
            mid_index = (first + last) // 2

            if input[mid_index] == mid_index:
                smallest_index = min(smallest_index, mid_index)
                last = mid_index - 1
            elif mid_index > input[mid_index]:
                first = mid_index + 1
            else:
                last = mid_index - 1

        return smallest_index if smallest_index != len(input) else -1


input1 = [-8, 0, 2, 5]
# expected = 2
input2 = [-1, 0, 3, 6]
# expected = -1
input3 = [0, 1, 2, 3, 4, 5, 6]
# expected = 0

print(Solution().ievs_bruteforce(input1))
print(Solution().ievs_binary_search(input1))

print(Solution().ievs_bruteforce(input2))
print(Solution().ievs_binary_search(input2))

print(Solution().ievs_bruteforce(input3))
print(Solution().ievs_binary_search(input3))
