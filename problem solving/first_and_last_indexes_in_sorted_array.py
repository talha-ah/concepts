class Solution(object):
    def fnlisa(self, numbers, target):
        """
        T=n
        S=1
        """

        result = [-1, -1]

        for i in range(len(numbers)):
            if numbers[i] == target:
                result[0] = i
                break
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] == target:
                result[1] = i
                break

        return result

    def fnlisa_binary_search(self, numbers, target):
        """
        T=n
        S=1
        """

        result = [-1, -1]

        for i in range(len(numbers)):
            if numbers[i] == target:
                result[0] = i
                break
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] == target:
                result[1] = i
                break

        return result


print(Solution().fnlisa([1, 2, 3, 4, 5, 9, 9, 9, 10], 9))
# expected = [5, 7]
