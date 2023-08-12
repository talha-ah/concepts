# The Fibonacci sequence is a series of numbers in which each number is the sum of the two that precede it


class Solution:
    def feb(self, n):
        """
        Recursive Solution
        T = O(2^n) - exponential
        """

        if n == 0 or n == 1:  # constant time
            return n

        return self.feb(n - 1) + self.feb(n - 2)  # exponential time (O(2^n))

    def feb_iteratively(self, n):
        """
        Recursive Solution
        T = O(n) - linear
        """

        stack = [n]

        sum = 0

        while len(stack) > 0:
            n = stack.pop()

            if n == 0 or n == 1:
                sum += n
            else:
                stack.append(n - 1)
                stack.append(n - 2)

        return sum

    def feb_memo(self, n, memo):
        """
        Memoization solution
        T = O(n) - linear
        """

        if memo[n] is not None:
            return memo[n]

        if n == 1 or n == 2:
            return 1

        result = self.feb(n - 1) + self.feb(n - 2)
        memo[n] = result
        return result


print(Solution().feb(10))
print(Solution().feb_iteratively(10))
