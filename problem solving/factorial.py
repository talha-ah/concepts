from math import factorial


class Solution(object):
    def factorial_recursively(self, input):
        """
        T = O(n)
        S = O(1)
        """

        if input <= 1:
            return input

        return input * self.factorial_recursively(input - 1)
        """
        Recursion
        return 5 * recurse(4)
                   return 4 * recurse(3)
                              return 3 * recurse(2)
                                         return 2 * recurse(1)
                                                    base case return 1
                                         return 2 = 2*1
                              return 6 = 3*2
                   return 24 = 4*6
        return 120 = 5*24
        """

    def factorial_iteratively(self, input):
        """
        T = O(n)
        S = O(1)
        """

        factorial = 1

        for i in range(1, input + 1):
            factorial *= i

        return factorial


number = 10

print(factorial(number))
print(Solution().factorial_recursively(number))
print(Solution().factorial_iteratively(number))
