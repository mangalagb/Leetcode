#Given a string s representing a valid expression, implement a basic calculator to evaluate it,
# and return the result of the evaluation.
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical
# expressions, such as eval().

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        postfix = []
        op_stack = []
        digit = 0
        digit_added = False

        for i in range(0, len(s)+1):
            if i == len(s):
                current = " "
            else:
                current = s[i]

            if current.isdigit():
                digit = (digit*10) + int(current)
                digit_added = True
            elif digit_added:
                postfix.append(digit)
                digit = 0
                digit_added = False

            if current == "(":
                op_stack.append(current)

            elif current == "+":
                # Operators of the same precedence cannot stay together
                if len(op_stack) > 0 and (op_stack[-1] == "-" or op_stack[-1] == "+"):
                    postfix.append(op_stack.pop())
                    op_stack.append(current)
                else:
                    op_stack.append(current)

            elif current == "-":
                # Operators of the same precedence cannot stay together
                if len(op_stack) == 0:
                    op_stack.append(current)
                elif op_stack[-1] == "+":
                    top = op_stack.pop()
                    postfix.append(top)
                    op_stack.append(current)
                elif s[i-1] == "(":
                    postfix.append(0)
                    op_stack.append("-")
                elif op_stack[-1] == "-":
                    top = op_stack.pop()
                    postfix.append(top)
                    op_stack.append(current)
                else:
                    op_stack.append(current)

            elif current == ")":
                while True:
                    top = op_stack.pop()
                    if top == "(":
                        break
                    postfix.append(top)

        #append all remaming symbols from stack
        while len(op_stack) > 0:
            postfix.append(op_stack.pop())

        #print(postfix)

        #Evaluate postfix expression
        stack = []
        for i in range(0, len(postfix)):
            current = postfix[i]

            if type(current) == int:
                stack.append(current)

            elif current == "+":
                a = stack.pop()
                b = stack.pop()

                result = b + a
                stack.append(result)
            elif current == "-":
                a = stack.pop()

                if len(stack) == 0:
                    result = -1*a
                else:
                    b = stack.pop()
                    result = b-a
                stack.append(result)

        answer = stack.pop()
        return answer

my_sol = Solution()

s = "1 + 1"
print(my_sol.calculate(s)) #2

s = " 2-1 + 2 "
print(my_sol.calculate(s)) #3

s = "(1+(4+5+2)-3)+(6+8)"
print(my_sol.calculate(s)) #23

s = "(2+1)-3"
print(my_sol.calculate(s)) #0

s = "15+(2-1)"
print(my_sol.calculate(s)) #16

s = "56789"
print(my_sol.calculate(s)) #56789

s = "-5"
print(my_sol.calculate(s)) #-5

s = "-(2 + 3)"
print(my_sol.calculate(s)) #-5

s = "0"
print(my_sol.calculate(s)) #0

s = "2-4-(8+2-6+(8+4-(1)+8-10))"
print(my_sol.calculate(s)) #-15

s = "1-(-2)"
print(my_sol.calculate(s)) #3