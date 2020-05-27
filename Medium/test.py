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
        nested_ans = None

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

                if nested_group or number_of_groups > 0:
                    nested_group = True

                word = ""
                while stack[0] != "[":
                    word = stack.pop(0) + word

                # Discard the [
                stack.pop(0)
                number_of_times = stack.pop(0)

                if nested_group:
                    if not nested_ans:
                        new_word = word * number_of_times
                        nested_ans = new_word
                    else:
                        new_word = ""
                        for i in range(0, number_of_times):
                            new_word = new_word + (word + nested_ans)
                        nested_ans = new_word
                else:
                    res = word * number_of_times
                    ans = ans + res

                if nested_group and number_of_groups == 0:
                    ans = ans + nested_ans

            elif push_to_stack:
                if not nested_group:
                    stack.insert(0, character)
                else:
                    nested_ans = nested_ans + character
            else:
                ans = ans + character

        return ans



my_sol = Solution()

s = "3[a]2[b4[F]c]"
print(my_sol.decodeString(s))  # aaabFFFFcbFFFFc
