#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        stack = []

        opening_braces = set()
        opening_braces.add("(")
        opening_braces.add("{")
        opening_braces.add("[")

        closing_braces = set()
        closing_braces.add(")")
        closing_braces.add("}")
        closing_braces.add("]")

        for character in s:
            if character in opening_braces:
                stack.append(character)
            elif character in closing_braces:
                if len(stack) == 0:
                    return False
                top_element = stack.pop(-1)

                if character is "}" and top_element != "{":
                    return False
                elif character is "]" and top_element != "[":
                    return False
                elif character is ")" and top_element != "(":
                    return False
        if len(stack) > 0:
            return False
        return True



my_sol = Solution()

s = "()[]{}"
print(my_sol.isValid(s)) #True

s = "()"
print(my_sol.isValid(s)) #True

s = "([)]"
print(my_sol.isValid(s)) #False

s = "(]"
print(my_sol.isValid(s)) #False

s = "{[]}"
print(my_sol.isValid(s)) #True

s = "("
print(my_sol.isValid(s)) #False
