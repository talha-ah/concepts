class Solution(object):
    def smallest_substring_of_all_characters(self, arr, s):

        j = 0
        answer = ""
        found = True
        for i in range(len(s)):
            if j >= len(arr) and found:
                return answer

            if s[i] == arr[j]:
                j += 1
                found = True
                answer += arr[j]
            else:
                j = 0
                found = False

        return "Not found"


print(Solution().smallest_substring_of_all_characters(["x", "y", "z"], "xyyzyzyx"))
# expected = zyx
