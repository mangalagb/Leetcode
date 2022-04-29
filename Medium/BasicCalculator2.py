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

        operator = "+"
        digit = 0
        stack = []

        for i in range(0, len(s) + 1):
            if i == len(s):
                current = "$"
            else:
                current = s[i]

            if current == " ":
                continue
            elif current.isdigit():
                digit = (digit * 10) + int(current)
            else:
                if operator == "+":
                    digit = digit * 1
                elif operator == "-":
                    digit = digit * -1
                elif operator == "*":
                    previous_num = stack.pop(-1)
                    digit = digit * previous_num
                elif operator == "/":
                    previous_num = stack.pop(-1)
                    digit = int(previous_num / digit)

                stack.append(digit)
                digit = 0
                operator = current

        result = 0
        for i in range(0, len(stack)):
            current = stack[i]
            result += current

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
