#Given the array nums, for each nums[i] find out how many numbers in the
# array are smaller than it. That is, for each nums[i] you have to count
# the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        frequency_map = {}
        largest_num = 100
        for i in range(0, largest_num+1):
            frequency_map[i] = [0]

        for i in range(0, len(nums)):
            num = nums[i]
            frequency_map[num][0] += 1
            frequency_map[num].append(i)

        result = [-1] * len(nums)
        count = 0

        for key, value in frequency_map.items():
            if len(value) > 1:
                number_of_times = value[0]
                indexes = value[1:]

                for index in indexes:
                    result[index] = count
                count += number_of_times
        return result

my_sol = Solution()

nums = [8,1,2,2,3]
print(my_sol.smallerNumbersThanCurrent(nums)) #[4,0,1,1,3]

nums = [6,5,4,8]
print(my_sol.smallerNumbersThanCurrent(nums)) #[2,1,0,3]

nums = [7,7,7,7]
print(my_sol.smallerNumbersThanCurrent(nums)) #[0,0,0,0]


