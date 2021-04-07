#Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')',
# in any positions ) so that the resulting parentheses string is valid and
# return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i = 0
        while True:
            if i >= len(s):
                break

            current = s[i]
            if current == "(":
                stack.append(i)
            elif current == ")":
                if len(stack) == 0:
                    s = self.remove_character(s, i)
                    i -= 1
                else:
                   stack.pop()
            i += 1

        while len(stack) > 0:
            s = self.remove_character(s, stack.pop())

        return s

    def remove_character(self, s, i):
        result = s[:i] + s[i+1:]
        return result


my_sol = Solution()

s = "lee(t(c)o)de)"
print(my_sol.minRemoveToMakeValid(s)) #"lee(t(co)de)" , "lee(t(c)ode)", "lee(t(c)o)de"

s = "a)b(c)d"
print(my_sol.minRemoveToMakeValid(s)) #"ab(c)d"

s = "))(("
print(my_sol.minRemoveToMakeValid(s)) #""

s = "(a(b(c)d)"
print(my_sol.minRemoveToMakeValid(s)) #"a(b(c)d)"

s = ""
print(my_sol.minRemoveToMakeValid(s)) #""

s = "(()()()"
print(my_sol.minRemoveToMakeValid(s)) #"()()()"

s = "(()()())"
print(my_sol.minRemoveToMakeValid(s)) #"(()()())"
