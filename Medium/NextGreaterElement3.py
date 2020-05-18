#Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the
# same digits existing in the integer n and is greater in value than n. If no such positive 32-bit
# integer exists, you need to return -1.

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [int(i) for i in str(n)]
        queue = []
        popped_element = None
        current_element = None

        for i in range(len(nums)-1, -1, -1):
            current = nums[i]
            current_element = [current, i]
            if len(queue) == 0:
                queue.insert(0, [current, i])

            else:
                top = queue[0]
                if current > top[0]:
                    queue.insert(0, [current, i])
                else:
                    while len(queue) != 0 and current < top[0]:
                        popped_element = queue.pop(0)

                    if popped_element:
                        break
                    queue.insert(0, [current, i])

        #Exchange
        if popped_element:
            index1 = current_element[1]
            num1 = current_element[0]

            index2 = popped_element[1]
            num2 = popped_element[0]

            nums[index1] = num2
            nums[index2] = num1

        result = nums[:current_element[1]+1]
        remaining_elements = sorted(nums[current_element[1]+1:])
        for remaining_num in remaining_elements:
            result.append(remaining_num)
        return result

my_sol = Solution()

num = 123
print(my_sol.nextGreaterElement(num)) #132

# num = 143
# print(my_sol.nextGreaterElement(num)) #314
#
# num = 1432
# print(my_sol.nextGreaterElement(num)) # 2134
#
# num = 500
# print(my_sol.nextGreaterElement(num)) #-1

# num = 506
# print(my_sol.nextGreaterElement(num)) #560
#
# num = 1234
# print(my_sol.nextGreaterElement(num)) #1243
#
# num = 101
# print(my_sol.nextGreaterElement(num)) #110
