# #Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#(Postfix notation. ie a+b is expressed as ab+)
#
# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
#
# Note that division between two integers should truncate toward zero.
#
# It is guaranteed that the given RPN expression is always valid. That means the
# expression would always evaluate to a result, and there will not be any division by zero operation.

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = set()
        operators.add("+")
        operators.add("-")
        operators.add("*")
        operators.add("/")

        for character in tokens:
            if character not in operators:
                stack.append(int(character))
            else:
                right = stack.pop(-1)
                left = stack.pop(-1)
                result = None
                if character == "+":
                    result = left + right
                elif character == "-":
                    result = left - right
                elif character == "*":
                    result = left * right
                elif character == "/":
                    result = int(float(left) / right)
                stack.append(result)
        ans = stack[0]
        return ans

my_sol = Solution()

tokens = ["2","1","+","3","*"]
print(my_sol.evalRPN(tokens)) #9

tokens = ["4","13","5","/","+"]
print(my_sol.evalRPN(tokens)) #6

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(my_sol.evalRPN(tokens)) #22
