class Solution(object):
    def iter(self, array):
        """
        T = O(n)
        S = O(1)
        """

        sum = 0

        for ele in array:
            sum += ele

        return sum

    def recur(self, array):
        """
        T = O(n)
        S = O(1)
        """

        if not len(array):
            return 0

        return array[0] + self.recur(array[1:])
        """
        Recursion
        return 1 + recurse([2,3,4,5])
                   return 2 + recurse([3,4,5])
                              return 3 + recurse([4,5])
                                         return 4 + recurse([5])
                                                    return 5 + recurse([])
                                                               base case 0
                                                    return 5 = 5+0
                                         return 9 = 4+5
                              return 12 = 3+9
                   return 14 = 2 + 12
        return 15 = 1 + 14
        """


array = [1, 2, 3, 4, 5]

print(sum(array))
print(Solution().iter(array))
print(Solution().recur(array))
