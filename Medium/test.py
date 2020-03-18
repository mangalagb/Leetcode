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
        new_nums = nums
        new_nums.extend(nums)
        length_of_array = len(new_nums)
        result = [-1] * len(new_nums)

        i = 0
        stack = []

        while True:
            if i == length_of_array:
                break

            current = new_nums[i]
            length_of_stack = len(stack)

            if length_of_stack == 0:
                stack.append(i)
                i += 1
                continue

            top_index = stack[length_of_stack-1]
            top_element = new_nums[top_index]

            if current < top_element:
                stack.append(i)
                i += 1
            elif current > top_element:
                if result[top_index] == -1:
                    result[top_index] = current
                    stack.pop()
            elif current == top_element:
                i += 1
                continue

        half_result = len(result) //2
        answer = [-1] * half_result
        for i in range(0, half_result):
            ans = result[i]
            if ans == -1:
                new_index = len(answer) + i
                if new_index < len(result):
                    ans = result[new_index]
            answer[i] = ans
        return answer

my_sol = Solution()

nums = [1,2,1]
print(my_sol.nextGreaterElements(nums)) #[2,-1,2]

nums = [1,2,3,2,1]
print(my_sol.nextGreaterElements(nums)) #[2,3,-1,3,2]

nums = [1,2,3,4,3]
print(my_sol.nextGreaterElements(nums)) #[2,3,4,-1,4]
