# #Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.
#
# Implement the ZigzagIterator class:
#
# ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
# boolean hasNext() returns true if the iterator still has elements, and false otherwise.
# int next() returns the current element of the iterator and moves the iterator to the next element

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.result = []
        l1 = len(v1)
        l2 = len(v2)

        if l1 == 0 and l2 > 0:
            self.result.extend(v2)
        elif l2 == 0 and l1 > 0:
            self.result.extend(v1)
        elif l1 == 0 and l2 == 0:
            self.result = []
        else:
            for num in v1:
                self.result.append(num)
                self.result.append(None)

            i = 1
            for num in v2:
                if i > len(v1):
                    self.result.append(num)
                elif self.result[i] is None:
                    self.result[i] = num
                    i += 2

        self.result = [i for i in self.result if i is not None]
        self.pointer = 0


    def next(self):
        """
        :rtype: int
        """
        number = self.result[self.pointer]
        self.pointer += 1
        return number


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.pointer < len(self.result):
            return True
        else:
            return False


v1 = [1,2]
v2 = [3,4,5,6]
my_sol = ZigzagIterator(v1,v2)
sol = []
while my_sol.hasNext():
    next_ele = my_sol.next()
    sol.append(next_ele)
print(sol) #[1,3,2,4,5,6]

v1 = [1]
v2 = []
my_sol = ZigzagIterator(v1,v2)
sol = []
while my_sol.hasNext():
    next_ele = my_sol.next()
    sol.append(next_ele)
print(sol) #[1]

v1 = []
v2 = [1]
my_sol = ZigzagIterator(v1,v2)
sol = []
while my_sol.hasNext():
    next_ele = my_sol.next()
    sol.append(next_ele)
print(sol) #[1]

v1 = [1,2]
v2 = []
my_sol = ZigzagIterator(v1,v2)
sol = []
while my_sol.hasNext():
    next_ele = my_sol.next()
    sol.append(next_ele)
print(sol) #[1,2]

v1= [1,2]
v2 = [3]
my_sol = ZigzagIterator(v1,v2)
sol = []
while my_sol.hasNext():
    next_ele = my_sol.next()
    sol.append(next_ele)
print(sol) #[1,3,2]

v1 = [1]
v2 = [2,3,4,5]
my_sol = ZigzagIterator(v1,v2)
sol = []
while my_sol.hasNext():
    next_ele = my_sol.next()
    sol.append(next_ele)
print(sol) #[1,2,3,4,5]