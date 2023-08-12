class Solution(object):
    def fib_recurse(self, n):
        """
        T = 2^n
        S = 1
        """

        if n < 0:
            return None
        if n <= 1:
            return n

        return self.fib_recurse(n - 1) + self.fib_recurse(n - 2)
        """
        Recursion - for 6
        return recurse(5) + recurse(4)
               return (recurse(4) + recurse(3)) + (recurse(3) + recurse(2))
                      return ((recurse(3) + recurse(2)) + (recurse(2) + recurse(1))) + ((recurse(2) + recurse(1)) + (recurse(1) + recurse(0)))
                            return ((recurse(2) + recurse(1)) + (recurse(1) + recurse(0))) + ((recurse(1) + recurse(0)) + base case 1) + (((recurse(1) + recurse(0)) + base case 1) + (base case 1 + base case 0))
                                  return (((recurse(1) + recurse(0)) + base case 1) + (1 + 0)) + ((base case 1 + base case 0) + 1) + ((base case 1 + base case 0) + 1) + (1+0))
                                        return ((base case 1 + base case 0) + 1) + 1 + ((1+0) + 1) + ((1+0)+1)+1
                                              return ((1+0)+1)+1+(1+1)+(1+1)+1
                                                    return (1+1)+1+(2)+(2)+1
                                                          return 2+1+2+2+1
                                                                return 8
        """

    def fib_iteratively(self, n):
        """
        T = n
        S = n
        """

        if n < 0:
            return None

        stack = [n]

        sum = 0

        while len(stack):
            n = stack.pop()

            if n <= 1:
                sum += n

            else:
                stack.append(n - 1)
                stack.append(n - 2)

        return sum

    def fib_bottom_up(self, n):
        """
        T = n
        S = n
        """

        if n <= 0:
            return None

        bottom_up = [1] * n

        for i in range(2, n):
            bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]

        return bottom_up[n - 1]

    def fib_memo(self, n, memo={}):
        """
        T = n
        S = n
        """

        if n <= 0:
            return None
        if n <= 2:
            return 1

        if n in memo:
            return memo[n]

        memo[n] = self.fib_memo(n - 1, memo) + self.fib_memo(n - 2, memo)

        return memo[n]


number = 6
# 1,1,2,3,5,8

print(Solution().fib_recurse(number))
print(Solution().fib_iteratively(number))
print(Solution().fib_bottom_up(number))
print(Solution().fib_memo(number))
