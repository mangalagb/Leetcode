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
        print(s, k)

        begin = 1
        end = 0
        length_of_string = len(s)
        count = 0
        index_where_character_changed = -1
        max_length = -1

        prev_char = s[0]
        while end < length_of_string:
            current_char = s[end]

            if end == begin or current_char == prev_char:
                end += 1

            elif current_char != prev_char:
                count += 1
                index_where_character_changed = end
                if count <= k:
                    end += 1
                else:
                    result = end - begin + 1
                    if result > max_length:
                        max_length = result
                    begin = index_where_character_changed
                    prev_char = current_char

        print(max_length)
        return max_length


my_sol = Solution()

s = "ABAB"
k = 2
my_sol.characterReplacement(s, k)

s = "AABABBA"
k = 1
my_sol.characterReplacement(s, k)