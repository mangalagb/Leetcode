#Given two arrays, write a function to compute their intersection.

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        counts = {}
        result = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result




my_sol = Solution()

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(my_sol.intersect(nums1, nums2)) #[4,9]

array1 = [1, 2, 2, 1]
array2 = [2, 2]
print(my_sol.intersect(array1, array2)) #[2, 2]
