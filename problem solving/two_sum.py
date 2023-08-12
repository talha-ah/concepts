from black import Set


class Solution(object):
    def two_sum_brute_force(self, numbers, target):
        """
        T=n^2
        S=1
        """

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return True

        return False

    def two_sum_hashmap(self, numbers, target):
        """
        T=n
        S=n
        """

        hashmap = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]

            if diff in hashmap.keys():
                return True
            else:
                hashmap[numbers[i]] = 1

        return False

    def two_sum_set(self, numbers, target):
        """
        T=n
        S=n
        """

        s = set()

        for i in range(len(numbers)):
            diff = target - numbers[i]

            if diff in s:
                return True
            else:
                s.add(numbers[i])

        return False


print(Solution().two_sum_brute_force([2, 7, 11, 15], 18))
print(Solution().two_sum_hashmap([2, 7, 11, 15], 18))
print(Solution().two_sum_set([2, 7, 11, 15], 18))
# expected = True (7+11=18)
