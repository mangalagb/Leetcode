class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        #print(nums, target)

        ans = 0
        abs_diff = 1000000000000000

        for k in range(0, len(nums) -2):

            i = k +1
            j = len(nums) -1

            while i < j:
                local_sum = nums[i] + nums[j] + nums[k]
                local_abs_difference = abs(local_sum - target)

                if local_abs_difference == 0:
                    ans = local_sum
                    return ans

                if local_abs_difference < abs_diff:
                    ans = local_sum
                    abs_diff = local_abs_difference

                elif local_sum > target:
                    j -= 1

                elif local_sum < target:
                    i += 1
        return ans






my_sol =  Solution()

nums = [-1, 2, 1, -4]
target = 1
print(my_sol.threeSumClosest(nums, target))

nums = [1,1,1,0]
target = 100
print(my_sol.threeSumClosest(nums, target))

nums = [1,1,1,0]
target = -100
print(my_sol.threeSumClosest(nums, target))

nums = [0,2,1,-3]
target = 1
print(my_sol.threeSumClosest(nums, target))

nums = [1,1,-1,-1,3]
target = -1
print(my_sol.threeSumClosest(nums, target))
