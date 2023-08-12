# Find the number of steps, which can be generated to reach the top of the stair of height n
# steps can be 1 or 2
# Same as fibonacci sequence


class Solution(object):
    def staircase_recursively(self, n):
        if n <= 1:
            return 1

        return self.staircase_recursively(n - 1) + self.staircase_recursively(n - 2)

    def staircase_iteratively(self, n):
        if n <= 1:
            return 1

        stack = [n]

        steps = 0
        while len(stack):
            n = stack.pop()

            if n <= 1:
                steps += 1
            else:
                stack.append(n - 1)
                stack.append(n - 2)

        return steps

    def staircase_bottom_up(self, n):
        if n <= 1:
            return 1

        bottom_up = [1] * n

        for i in range(2, n):
            bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]

        return bottom_up[n - 1] + bottom_up[n - 2]


height = 5


print(Solution().staircase_recursively(height))
print(Solution().staircase_iteratively(height))
print(Solution().staircase_bottom_up(height))

# Find the number of steps, which can be generated to reach the top of the stair of height n
# but with given steps


class Solution2(object):
    def staircase_recursively(self, n, steps):
        if n == 0:
            return 1

        total = 0

        for i in steps:
            if n - i >= 0:
                total += self.staircase_recursively(n - i, steps)

        return total

    def staircase_bottom_up(self, n, steps):
        if n == 0:
            return 1

        bottom_up = [1] * n

        for i in range(2, n):
            total = 0
            for j in steps:
                if i - j >= 0:
                    total += bottom_up[i - j]
            bottom_up[i] = total

        return bottom_up[n - 1] + bottom_up[n - 2]


steps = [1, 3, 5]

print(Solution2().staircase_recursively(height, steps))
print(Solution2().staircase_bottom_up(height, steps))
