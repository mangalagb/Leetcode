#Given a list of daily temperatures T, return a list such that, for each day in the input,
# tells you how many days you would have to wait until a warmer temperature. If there is no
# future day for which this is possible, put 0 instead.

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        days = [0] * len(T)
        for i in range(0, len(T)):
            current = T[i]

            if len(stack) == 0:
                stack.append([current, i])
                continue

            top = stack[0][0]
            if current < top:
                stack.insert(0, [current, i])
            else:
                while len(stack) > 0 and current > stack[0][0]:
                    popped_element = stack.pop(0)
                    popped_element_index = popped_element[1]
                    days[popped_element_index] = i

                stack.insert(0, [current, i])

        for i in range(0, len(days)):
            if days[i] != 0:
                number_of_days = days[i] - i
                days[i] = number_of_days
        return days

my_sol = Solution()

T = [73, 74, 75, 71, 69, 72, 76, 73]
#   [74, 75, 76, 72, 72, 76, 0,  0]
O = [1, 1, 4, 2, 1, 1, 0, 0]
print(my_sol.dailyTemperatures(T))
