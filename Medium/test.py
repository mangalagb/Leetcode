# Given a circular array (the next element of the last element is the first element of the array),
# print the Next Greater Number for every element. The Next Greater Number of a number x is the first
# greater number to its traversing-order next in the array, which means you could search circularly to
# find its next greater number. If it doesn't exist, output -1 for this number.

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length_of_nums = len(nums)
        queue = []
        result = [-1] * length_of_nums

        for i in range(0,length_of_nums):
            current = nums[i]
            self.find_greater(current, i, queue, result)

        for i in range(0,length_of_nums):
            current = nums[i]
            self.find_greater(current, i, queue, result)

        return result

    def find_greater(self, current, i, queue, result):
        len_of_queue = len(queue)

        if len_of_queue == 0:
            queue.insert(0, [current, i])
        else:
            top = queue[0]

            if current < top[0]:
                queue.insert(0, [current, i])
            else:
                while len(queue) != 0 and current > queue[0][0]:
                    popped_element = queue.pop(0)
                    result[popped_element[1]] = current

                queue.insert(0, [current, i])

my_sol = Solution()

nums = [1,2,1]
print(my_sol.nextGreaterElements(nums)) #[2,-1,2]

nums = [1,2,3,2,1]
print(my_sol.nextGreaterElements(nums)) #[2,3,-1,3,2]

nums = [1,2,3,4,3]
print(my_sol.nextGreaterElements(nums)) #[2,3,4,-1,4]
