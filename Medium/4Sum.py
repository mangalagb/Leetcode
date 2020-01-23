# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in
# nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        result = set()

        for i in range(0, len(sorted_nums)):
            fourth_num = sorted_nums[i]
            list_without_num = sorted_nums[i+1:]
            remaining_sum = target - fourth_num
            three_sum = self.threeSum(list_without_num, remaining_sum)
            if len(three_sum) > 0:
                for elements in three_sum:
                    elements.insert(0, fourth_num)
                    new_list = sorted(elements)
                    result.add(str(new_list))

        elements = []
        for ans in result:
            num = ans[1:len(ans)-1]
            str_numbers = num.split(",")
            numbers = [int(i) for i in str_numbers]
            elements.append(numbers)

        return elements

    def threeSum(self, nums, target):
        if not nums:
            return []

        result = []
        unique_numbers = set()
        for k in range(len(nums)):
            sum_to_find = target - nums[k]

            i = k+1
            j = len(nums) - 1

            while i < j:
                if nums[i] + nums[j] == sum_to_find:
                    string_num = str(nums[k]) + str(nums[i]) + str(nums[j])

                    if string_num not in unique_numbers:
                        result.append([nums[k], nums[i], nums[j]])
                        unique_numbers.add(string_num)
                    result.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < sum_to_find:
                    i += 1
                else:
                    j -= 1
        return result


my_sol = Solution()

nums = [1,0,-1,0,-2,2]
target = 0
print(my_sol.fourSum(nums, target))

ans = [
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

#[[-1,-1,0,2],[-1,0,0,1],[-2,0,1,1],[-1,-1,1,1],[-2,0,0,2],[-2,-1,1,2]]
