# Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
#
# In one operation, you can choose any character of the string and change it to any other uppercase English character.
#
# Find the length of the longest sub-string containing all repeating letters you can get after performing
# the above operations.
# Note:
# Both the string's length and k will not exceed 10^4.

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        characters = {}
        end = 0
        begin = 0

        count = 0
        result = 0

        while end < len(s):
            character = s[end]

            #Add initial char
            if len(characters) == 0:
                characters[character] = 1
            elif character in characters:
                characters[character] += 1
            elif count+1 <= k:
                characters[character] = 1
            else:
                characters[character] = 1
                count += 1

            if len(characters) > 1:
                count = max(count, min(characters.values()))

            if count <= k:
                local_result = end - begin + 1
                result = max(result, local_result)
            end += 1

            while count > k:
                #print("incorrect answer")

                begin_char = s[begin]
                characters[begin_char] -= 1
                if characters[begin_char] == 0:
                    characters.pop(begin_char)
                begin += 1
                if len(characters) == 1:
                    count = 0
                else:
                    count = min(characters.values())

        return result



my_sol = Solution()

s = "ABAB"
k = 2
print(my_sol.characterReplacement(s, k))

s = "AABABBA"
k = 1
print(my_sol.characterReplacement(s, k))

s = "ABAA"
k = 0
print(my_sol.characterReplacement(s, k))

s = "BAAA"
k = 0
print(my_sol.characterReplacement(s, k))

s = "ABBB"
k = 2
print(my_sol.characterReplacement(s, k))

s = "ABCDE"
k = 1
print(my_sol.characterReplacement(s, k))

