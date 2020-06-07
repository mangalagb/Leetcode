# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
# exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for
# those repeat numbers, k. For example, there won't be input like 3a or 2[4].

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        character_stack = []
        number_stack = []
        number = ""

        for i in range(0, len(s)):
            character = s[i]

            if character.isnumeric():
                number += character
            elif character == "[":
                number_stack.insert(0, int(number))
                number = ""
                character_stack.insert(0, "[")
            elif character == "]":
                word = ""
                while character_stack[0] != "[":
                    element = character_stack.pop(0)
                    word = element + word

                # Remove the [
                character_stack.pop(0)
                number_of_times = number_stack.pop(0)
                new_word = word * number_of_times
                character_stack.insert(0, new_word)
            else:
                character_stack.insert(0, character)

        result = ""
        for value in character_stack:
            result = value + result
        return result


my_sol = Solution()

# s = "3[a]2[bc]"
# print(my_sol.decodeString(s))  # "aaabcbc"
#
# s = "2[abc]3[cd]ef"
# print(my_sol.decodeString(s))  # abcabccdcdcdef
#
# s = "3[a2[c]]"
# print(my_sol.decodeString(s))  # accaccacc
#
# s = "3[a2[c]]3[a]2[bc]"
# print(my_sol.decodeString(s))  # accaccaccaaabcbc

s = "3[a]2[b4[F]c]"
print(my_sol.decodeString(s))  # aaabFFFFcbFFFFc
