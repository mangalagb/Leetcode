class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_elements = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        #If min stack is empty or current element is less than top of min stack
        if len(self.min_elements) == 0 or x <= self.min_elements[-1]:
            self.min_elements.append(x)

        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        popped_element = self.stack.pop(-1)

        #If popped element is the current min, then remove it from min stack too
        if popped_element == self.min_elements[-1]:
            self.min_elements.pop(-1)


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_elements[-1]

# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin()) # return -3
# minStack.pop()
# print(minStack.top())   # return 0
# print(minStack.getMin())  # return -2

minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.getMin())  # return -2
