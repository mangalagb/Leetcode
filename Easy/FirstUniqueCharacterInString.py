# Given a string, find the first non-repeating character in it and
# return it's index. If it doesn't exist, return -1.


class Solution(object):
    def firstUniqChar(self, s):
        repeated_set = set()
        unique_set = set()

        for character in s:
            if character in repeated_set:
                continue
            elif character not in repeated_set and character in unique_set:
                unique_set.remove(character)
                repeated_set.add(character)
            else:
                unique_set.add(character)

        for i in range(0, len(s)):
            character = s[i]
            if character in unique_set:
                return i
        return -1


my_sol = Solution()

s = "leetcode"
print(s,my_sol.firstUniqChar(s))

s = "loveleetcode"
print(s,my_sol.firstUniqChar(s))