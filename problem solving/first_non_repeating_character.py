class Solution(object):
    def fnrc_bruteforce(self, string):
        """
        T = n^2
        S = 1
        """

        for i in range(0, len(string)):
            non_duplicated = string[i]
            for j in range(0, len(string)):
                if i != j and string[i] == string[j]:
                    non_duplicated = None

            if non_duplicated:
                return non_duplicated

        return None

    def fnrc(self, string):
        """
        T = n
        S = n
        """

        hashmap = {}

        for i in range(0, len(string)):
            if string[i] in hashmap.keys():
                hashmap[string[i]] += 1
            else:
                hashmap[string[i]] = 1

        for key in hashmap.keys():
            if hashmap[key] == 1:
                return key

        return None

    def fnrc_with_find(self, string):
        """
        T = n
        S = 1
        """

        for i in range(len(string)):
            if string.find(string[i]) == string.rfind(string[i]):
                return string[i]

        return None

    def fnrc_with_indexing(self, string):
        """
        T = n
        S = 1
        """

        for i in range(len(string)):
            if string.index(string[i]) == string.rindex(string[i]):
                return string[i]

        return None


print(Solution().fnrc_bruteforce("aaabcccdeeef"))
print(Solution().fnrc_bruteforce("abcbad"))
print(Solution().fnrc_bruteforce("abcabcabc"))

print(Solution().fnrc("aaabcccdeeef"))
print(Solution().fnrc("abcbad"))
print(Solution().fnrc("abcabcabc"))

print(Solution().fnrc_with_find("aaabcccdeeef"))
print(Solution().fnrc_with_find("abcbad"))
print(Solution().fnrc_with_find("abcabcabc"))

print(Solution().fnrc_with_indexing("aaabcccdeeef"))
print(Solution().fnrc_with_indexing("abcbad"))
print(Solution().fnrc_with_indexing("abcabcabc"))
