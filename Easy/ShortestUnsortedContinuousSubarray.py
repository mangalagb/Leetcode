# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_of_array = len(nums)
        if length_of_array == 0 or length_of_array == 1:
            return 0

        i = 1
        prev = nums[0]
        incorrect_number = -1
        left_boundary = None

        while i < length_of_array:
            current = nums[i]
            if current < prev:
                incorrect_number = current
                left_boundary = i - 1
                break
            i += 1
            prev = current

        remaining_array = nums[i:]
        if len(remaining_array) > 0:
            minimum_number = min(remaining_array)
            if minimum_number <= incorrect_number:
                incorrect_number = minimum_number

        j = 0
        while left_boundary and j < length_of_array:
            if nums[j] > incorrect_number:
                left_boundary = j
                break
            j += 1

        #print(left_boundary, incorrect_number)

        k = length_of_array - 2
        prev = nums[length_of_array - 1]
        right_boundary = None
        incorrect_number = -1

        while k >= 0:
            current = nums[k]
            if current > prev:
                incorrect_number = current
                right_boundary = k + 1
                break
            k -= 1
            prev = current

        remaining_array = nums[:k]
        if len(remaining_array) > 0:
            maximum_number = max(remaining_array)
            if maximum_number >= incorrect_number:
                incorrect_number = maximum_number

        l = length_of_array - 1
        while right_boundary and l >= 0:
            if nums[l] < incorrect_number:
                right_boundary = l
                break
            l -= 1

        #print(right_boundary, incorrect_number)

        result = 0
        if left_boundary is not None and right_boundary is not None:
            result = right_boundary - left_boundary + 1
        return result







my_sol = Solution()

nums = [2, 6, 4, 8, 10, 9, 15]
print(my_sol.findUnsortedSubarray(nums))

nums = [1,2,4,5,3]
print(my_sol.findUnsortedSubarray(nums))

nums = [2,1]
print(my_sol.findUnsortedSubarray(nums))

nums = [5,4,3,2,1]
print(my_sol.findUnsortedSubarray(nums))

nums = [1,3,2,2,2]
print(my_sol.findUnsortedSubarray(nums))

nums = [2,1,1,1,1]
print(my_sol.findUnsortedSubarray(nums))

nums = [1,3,5,4,2]
print(my_sol.findUnsortedSubarray(nums))

nums = [1,2,3,4]
print(my_sol.findUnsortedSubarray(nums))
