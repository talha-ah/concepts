class Solution(object):
    def valid_parenthesis(self, s: str) -> bool:
        """
        T= n linear
        S= n linear
        """

        stack = []

        for i in range(len(s)):
            if s[i] in ["(", "{", "["]:
                stack.append(s[i])

            if s[i] == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False

            if s[i] == "}":

                if len(stack) == 0 or stack.pop() != "{":
                    return False

            if s[i] == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    return False

        return True if len(stack) == 0 else False


input = "()"
# expected = True
input = "()[]{}"
# expected = True
input = "(]"
# expected = False
input = "({[]})"
# expected = True
input = "({[]}}"
# expected = False
input = "["
# expected = False
input = "]"
# expected = False

print(Solution().valid_parenthesis(input))
