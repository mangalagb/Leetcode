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
        stack = []
        number_of_groups = 0
        number = ""
        ans = ""
        push_to_stack = False
        nested_group = False

        for character in s:
            if character.isnumeric():
                number += character
            elif character == "[":
                stack.insert(0, int(number))
                number = ""
                number_of_groups += 1
                stack.insert(0, "[")
                push_to_stack = True
            elif character == "]":
                push_to_stack = False
                number_of_groups -= 1
                if number_of_groups != 0:
                    nested_group = True

                word = ""
                while stack[0] != "[":
                    word = stack.pop(0) + word

                # Discard the [
                stack.pop(0)
                number_of_times = stack.pop(0)

                if number_of_groups > 0 or nested_group:
                    previous_word = ans
                    new_word = word + previous_word
                    ans = new_word * number_of_times
                else:
                    ans = ans + (word * number_of_times)

                #Reset flag
                if number_of_groups == 0:
                    nested_group = False
            elif push_to_stack:
                stack.insert(0, character)
            else:
                ans = ans + character

        return ans



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
