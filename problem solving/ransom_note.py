class Solution(object):
    def get_ransom_note_brute_force(self, characters, word):
        """
        T=n*m
        S=1
        """

        for i in range(len(word)):
            index = -1

            for j in range(len(characters)):
                if word[i] == characters[j]:
                    index = i

            if index == -1:
                return False

            characters[index] = -1

        return True

    def get_ransom_note(self, characters, word):
        """
        T=n
        S=n
        """

        hashmap = {}

        for i in range(len(characters)):
            if characters[i] in hashmap.keys():
                hashmap[characters[i]] += 1
            else:
                hashmap[characters[i]] = 1

        for i in range(len(word)):
            if word[i] not in hashmap.keys():
                return False
            else:
                if hashmap[word[i]] == 0:
                    return False
                else:
                    hashmap[word[i]] -= 1

        return True

    def brute_force(self, array, spell):
        """
        O(m^n)
        """
        for char in spell:
            if not char in array:
                return False

        return True

    def hash(self, array, spell):
        """
        O(n x m)
        """
        hash = {}

        for elem in array:
            if elem in hash.keys():
                hash[elem] = hash[elem] + 1
            else:
                hash[elem] = 1

        for char in spell:
            if not char in hash.keys():
                return False
            else:
                if hash[char] > 1:
                    hash[char] = hash[char] - 1
                else:
                    del hash[char]

        return True


print(Solution().get_ransom_note(["A", "B", "C", "D", "E", "F"], "BED"))
# expected true
print(Solution().get_ransom_note(["A", "B", "C", "D", "E", "F"], "CAT"))
# expected false
