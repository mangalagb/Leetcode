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
        i = 0
        j = 1
        length_of_string = len(s)
        count = 0
        max_length = -1
        possible_characters = {}
        previous_char = s[0]

        while j < length_of_string:
            character = s[j]

            if character in possible_characters:
                possible_characters[character] = 1

            if character not in possible_characters and len(possible_characters) > 1:
                count += 1







    def characterReplacement1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = 0
        j = 1
        length_of_string = len(s)
        count = 0
        prev_char = s[0]
        max_length = -1
        possible_characters = {}

        while j < length_of_string:
            current_char = s[j]

            if current_char == prev_char:
                j += 1
            elif current_char != prev_char and count < k:
                j += 1
                count += 1
                possible_characters.append(prev_char)
                possible_characters.append(current_char)
            else:
                i += 1
                prev_char = s[i]
                possible_characters.remove(s[i-1])
            result = j - i
            if result > max_length:
                max_length = result

        return max_length

my_sol = Solution()

# s = "ABAB"
# k = 2
# print(my_sol.characterReplacement1(s, k))
#
# s = "AABABBA"
# k = 1
# print(my_sol.characterReplacement1(s, k))
#
# s = "ABAA"
# k = 0
# print(my_sol.characterReplacement1(s, k))
#
# s = "BAAA"
# k = 0
# print(my_sol.characterReplacement1(s, k))

s = "ABBB"
k = 2
print(my_sol.characterReplacement(s, k))

