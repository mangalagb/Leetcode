# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {0: 0, 1: 0}

        for num in nums:
            num_dict[num] += 1


        begin = 0
        end = len(nums) - 1
        result = 0
        while True:
            number_of_zero = num_dict[0]
            number_of_one = num_dict[1]

            if number_of_zero == number_of_one:
                result = number_of_one * 2
                break

            number_to_remove = 0
            if number_of_one > number_of_zero:
                number_to_remove = 1

            if nums[begin] == number_to_remove:
                begin += 1
                num_dict[number_to_remove] -= 1
                continue

            end -= 1
            num_dict[number_to_remove] -= 1

        return result




my_sol = Solution()

# nums = [0,1]
# print(my_sol.findMaxLength(nums))
#
# nums = [0,1,0]
# print(my_sol.findMaxLength(nums))
#
# nums = [0,0,1,0,0,0,1,1]
# print(my_sol.findMaxLength(nums))
#
# nums = [1,1,1,1,1,1,1,1]
# print(my_sol.findMaxLength(nums))

nums = [0,1,1,0,1,1,1,0]
print(my_sol.findMaxLength(nums))

