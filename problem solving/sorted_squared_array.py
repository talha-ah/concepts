"""

Return a sorted squared array

Input 1 = [-7,-3,-1,4,8,12] => [1,9,16,49,64,144]
Input 2 = [1,2,3] => [1,4,9]
Input 3 = [-3,-2,-1] => [1,4,9]

"""


class Solution(object):
    def sorted_squared_array_bruteforce(self, input):
        """
        T = O(n log n)
        S = O(1)
        """

        for i in range(len(input)):
            input[i] = input[i] * input[i]

        input = sorted(input)

        return input

    def sorted_squared_array(self, input):

        """ """

        output = [0] * len(input)

        first = 0
        last = len(input) - 1

        for i in range(len(input) - 1, -1, -1):
            first_squared = input[first] * input[first]
            last_squared = input[last] * input[last]

            if last_squared > first_squared:
                output[i] = last_squared
                last -= 1
            else:
                output[i] = first_squared
                first += 1

        return output


input = [-7, -3, -1, 4, 8, 12]
# expected = [1,9,16,49,64,144]
input2 = [1, 2, 3]
# expected = [1,4,9]
input3 = [-3, -2, -1]
# expected = [1,4,9]

print(Solution().sorted_squared_array_bruteforce(input[:]))
print(Solution().sorted_squared_array_bruteforce(input2[:]))
print(Solution().sorted_squared_array_bruteforce(input3[:]))

print(Solution().sorted_squared_array(input))
print(Solution().sorted_squared_array(input2))
print(Solution().sorted_squared_array(input3))
