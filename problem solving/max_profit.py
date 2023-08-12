class Solution(object):
    """
    @profits = input array of profits
    @n = skip elements after every 2 elements in calculation
    """

    def max_profit(self, profits, n):

        max_profit = float("-inf")

        for i in range(0, len(profits)):
            sum = 0
            elems = n
            for j in range(i, len(profits) + i):
                if elems == 0 and n != 1:
                    elems = n
                else:
                    elems -= 1
                    index = j if j < len(profits) else j % len(profits)
                    sum += profits[index]

            if sum > max_profit:
                max_profit = sum

        return max_profit


print(Solution().max_profit([1, 5, 1, 3, 7, -3], 2))
# 1+5+3+7=16  ,  5+1+7-3=10  ,  1+3-3+1 = 2
# expected = 16
print(Solution().max_profit([3, -5], 1))
# expected = -2
print(Solution().max_profit([-3, 6, 3, -6], 1))
# expected = 0
print(Solution().max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
# expected = 39
print(
    Solution().max_profit(
        [1, -2, -3, 4, -5, 6, -7, 8, 9, 10, -11, 12, -13, 14, 15, 16, -17, 18, -19, 20],
        6,
    )
)
# expected = 54
