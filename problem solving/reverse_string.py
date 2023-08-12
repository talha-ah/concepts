class Solution(object):
    def reverse_iteratively(self, input):
        reversed = ""

        for cha in range(len(input) - 1, -1, -1):
            reversed += input[cha]

        return reversed

    def reverse_iteratively_2(self, input):
        reversed = ""

        for i in range(0, len(input)):
            reversed += input[len(input) - (i + 1)]

        return reversed

    def reverse_recursively(self, input):
        if len(input) <= 1:
            return input

        return input[len(input) - 1] + self.reverse_recursively(input[: len(input) - 1])

        """
        Recursive steps
        1- return 'a' + recurse('Talh')
        2-              return 'h' + recurse('Tal')
        3-                           return 'l' + recurse('Ta')
        4-                                        return 'a' + recurse('T')
        5-                                                     base case return 'T'
        6-                                        'aT'
        7-                           'laT'
        8-              'hlaT'
        9-  'ahlaT'
        """


print(Solution().reverse_iteratively("Talha"))
print(Solution().reverse_iteratively_2("Talha"))
print(Solution().reverse_recursively("Talha"))
