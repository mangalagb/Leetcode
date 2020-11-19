#Given two arrays, write a function to compute their intersection.

from collections import defaultdict

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        result = self.find_elements(nums1, nums2)
        return result


    def find_elements(self, array1, array2):
        num_dict = defaultdict(int)
        for current in array1:
            num_dict[current] += 1

        match_dict = defaultdict(int)
        for num in array2:
            if num in num_dict:
                if num_dict[num] != 0:
                    num_dict[num] -= 1
                    match_dict[num] += 1

        result = []
        for key, val in match_dict.items():
            temp = [key] * val
            result.extend(temp)
        return result


my_sol = Solution()

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(my_sol.intersect(nums1, nums2)) #[4,9]

array1 = [1, 2, 2, 1]
array2 = [2, 2]
print(my_sol.intersect(array1, array2)) #[2, 2]

array1 = [2,1]
array2 = [1,2]
print(my_sol.intersect(array1, array2)) #[1, 2]

array1 = [4,7,9,7,6,7]
array2 = [5,0,0,6,1,6,2,2,4]
print(my_sol.intersect(array1, array2)) #[4,6]
