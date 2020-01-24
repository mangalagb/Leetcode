class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow_initail = nums[0]
        fast_initail = nums[0]
        first_run = True
        result = None

        while True:
            if first_run:
                fast = fast_initail
                slow = slow_initail
                first_run = False

            fast_index = nums[fast]
            fast = nums[fast_index]

            slow = nums[slow]

            if fast == slow:
                result = nums[slow]
                break

        return result

my_sol = Solution()

nums = [1,3,4,2,2]
print(my_sol.findDuplicate(nums))

# nums = [3,1,3,4,2]
# print(my_sol.findDuplicate(nums))
#
# nums = [2,5,9,6,9,3,8,9,7,1]
# print(my_sol.findDuplicate(nums))
