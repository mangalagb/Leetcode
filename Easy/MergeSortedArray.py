# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Note:The number of elements initialized in nums1 and nums2 are m and n respectively.
#     You may assume that nums1 has enough space (size that is greater or equal to m + n)
#     to hold additional elements from nums2.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        num1_pointer = m-1
        num2_pointer = n-1
        for i in reversed(range(len(nums1))):
            if num1_pointer >= 0 and num2_pointer < 0:
                nums1[i] = nums1[num1_pointer]
                num1_pointer -= 1

            elif num1_pointer < 0 and num2_pointer >= 0:
                nums1[i] = nums2[num2_pointer]
                num2_pointer -= 1

            else:
                if nums1[num1_pointer] >= nums2[num2_pointer]:
                    nums1[i] = nums1[num1_pointer]
                    num1_pointer -= 1
                else:
                    nums1[i] = nums2[num2_pointer]
                    num2_pointer -= 1
        print(nums1)

my_sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
my_sol.merge(nums1, m, nums2, n)

