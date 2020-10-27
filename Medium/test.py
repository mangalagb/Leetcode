class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) == 1:
            return []

        length_of_nums = len(nums)
        left = [1] * length_of_nums
        right = [1] * length_of_nums
        result = [1] * length_of_nums

        product = 1
        for i in range(0, len(nums)):
            left[i] = product
            product *= nums[i]

        product = 1
        for i in range(length_of_nums-1, -1, -1):
            right[i] = product
            product *= nums[i]

        for i in range(0, length_of_nums):
            left_product = left[i]
            right_product = right[i]

            product = left_product * right_product
            result[i] = product
        return result




my_sol = Solution()

nums = [1,2,3,4]
print(my_sol.productExceptSelf(nums)) #[24,12,8,6]