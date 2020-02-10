class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length_of_array = len(nums) - 1

        if length_of_array == 0:
            return True

        queue = [length_of_array]

        while len(queue) > 0:
            element = queue.pop()
            result = self.do_jump(nums, element)
            if result is None:
                return True
            queue.extend(result)

        return False


    def do_jump(self, nums, index):
        local_queue = []

        count = 1
        for i in range(index-1, -1, -1):
            if nums[i] >= count:

                if i == 0:
                    return None

                local_queue.append(i)
            count += 1
        return local_queue



my_sol = Solution()

# nums = [2,3,1,1,4]
# print(my_sol.canJump(nums))
#
# nums = [3,2,1,0,4]
# print(my_sol.canJump(nums))
#
# nums = [0]
# print(my_sol.canJump(nums))

nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
print(my_sol.canJump(nums))
