# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue
# should support all the functions of a normal queue (push, peek, pop, and empty).
#
# Implement the MyQueue class:
#
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:
#
# You must use only standard operations of a stack, which means only push to top, peek/pop
# from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a
# stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
# Follow-up: Can you implement the queue such that each operation is amortized O(1) time
# complexity? In other words, performing n operations will take overall O(n) time even
# if one of those operations may take longer.

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        element = -1
        if len(self.stack2) > 0:
            top2 = len(self.stack2) - 1
            element = self.stack2.pop(top2)

        elif len(self.stack1) > 0:
            top1 = len(self.stack1) - 1
            for i in range(top1, -1, -1):
                current = self.stack1.pop(i)
                self.stack2.append(current)

            top2 = len(self.stack2) - 1
            element = self.stack2.pop(top2)
        return element


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        element = -1
        if len(self.stack2) > 0:
            top2 = len(self.stack2) - 1
            element = self.stack2[top2]

        elif len(self.stack1) > 0:
            temp = []
            top1 = len(self.stack1) - 1
            for i in range(top1, -1, -1):
                current = self.stack1[i]
                temp.append(current)

            top2 = len(temp) - 1
            element = temp[top2]
        return element

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:

myQueue = MyQueue()
myQueue.push(1) # queue is: [1]
myQueue.push(2) #queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek()) # return 1
print(myQueue.pop()) # return 1, queue is [2]
print(myQueue.empty()) # return false