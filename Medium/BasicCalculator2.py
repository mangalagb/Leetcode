# Given a string s which represents an expression, evaluate this
# expression and return its value.
#
# The integer division should truncate toward zero.

#If we look at the above examples, we can make the following observations -
#
# If the current operation is addition (+) or subtraction (-), then the expression
# is evaluated based on the precedence of the next operation.
# In example 1, 4+3 is evaluated later because the next operation is
# multiplication (3*5) which has higher precedence. But, in example 2, 4+3 is
# evaluated first because the next operation is subtraction (3-5) which has equal precedence.
#
# If the current operator is * or /,
# then the expression is evaluated irrespective of the next operation.
# This is because in the given set of operations (+,-,*,/),
# the * and / operations have the highest precedence and therefore must be evaluated first.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        number = 0
        sign = "+"
        stack = []
        s = s.strip()

        for i in range(0, len(s)):
            current = s[i]

            if current is " ":
                continue
            elif current.isdigit():
                number = (number*10) + int(current)

            if i == len(s)-1 or (current in ["+", "-", "*", "/"]):
                if sign == "+":
                    stack.append(number)
                elif sign == "-":
                    stack.append(-number)
                elif sign == "*":
                    result = stack.pop(-1) * number
                    stack.append(result)
                else:
                    result = int(stack.pop(-1) / number)
                    stack.append(result)
                number = 0
                sign = current

        result = 0
        for i in range(0, len(stack)):
            result += stack[i]
        return result







my_sol = Solution()

s = "14-3/2"
print(my_sol.calculate(s)) #13
#
# s = "3+2*2"
# print(my_sol.calculate(s)) #7
#
# s = "3*2+2"
# print(my_sol.calculate(s)) #8
#
# s = " 3/2 "
# print(my_sol.calculate(s)) #1
#
# s = " 3+5 / 2 "
# print(my_sol.calculate(s)) #5
#
# s = " 33+5 / 2 "
# print(my_sol.calculate(s)) #35
#
# s = " 100/5 / 2 "
# print(my_sol.calculate(s)) #10
#
# s = "1-1+1"
# print(my_sol.calculate(s)) #1
#
# s = "3/2"
# print(my_sol.calculate(s)) #1
#
# s = "2-3+4"
# print(my_sol.calculate(s)) #3
