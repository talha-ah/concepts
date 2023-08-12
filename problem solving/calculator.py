class Solution(object):
    def __is_integer(self, n: str or int) -> bool:
        try:
            int(n)
        except ValueError:
            return False
        else:
            return isinstance(int(n), int)

    def calculate(self, input: str = "") -> int:

        sign = "+"
        result = 0

        stack = []

        for i in range(len(input)):

            if self.__is_integer(input[i]):
                if sign == "+":
                    result += int(input[i])
                if sign == "-":
                    result -= int(input[i])

            elif input[i] == "-":
                sign = "-"

            elif input[i] == "+":
                sign = "+"

            elif input[i] == "(":
                stack.append(result)
                stack.append(sign)

                sign = "+"
                result = 0

            elif input[i] == ")":
                sign = stack.pop()

                if sign == "-":
                    result = -result

                result += stack.pop()

        return result

    def calculate_2(self, input: str = "") -> int:

        sign = "+"
        result = 0

        stack = []

        i = 0
        while i < len(input):

            if self.__is_integer(input[i]):
                num = ""

                while i < len(input) and self.__is_integer(input[i]):
                    num += input[i]
                    i += 1

                if sign == "+":
                    result += int(num)
                if sign == "-":
                    result -= int(num)

            elif input[i] == "-":
                sign = "-"

            elif input[i] == "+":
                sign = "+"

            elif input[i] == "(":
                stack.append(result)
                stack.append(sign)

                sign = "+"
                result = 0

            elif input[i] == ")":
                sign = stack.pop()

                if sign == "-":
                    result = -result

                result += stack.pop()

        return result


input = "( 1+1 )"
# expected = 2
input = "( 2-1 +2 )"
# expected = 3
input = "((1+(4+5+2)-3)+(6+8))"
# expected = 23
input = "-(3+(2-1))"
# expected = -4
input = "2+(1+(4+5+2)-3)+(6+8)"
# expected = 25
# input = "2147483647"
# expected = 2147483647 (works with calculate_2)

print(Solution().calculate(input))
