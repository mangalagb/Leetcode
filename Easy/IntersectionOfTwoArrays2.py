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

        #Find nums1 in nums2
        result1 = self.find_elements(nums1, nums2)
        result2 = self.find_elements(nums2, nums1)

        if len(result1) > len(result2):
            return result1
        else:
            return result2


    def find_elements(self, array1, array2):
        # Find array1 elements in array2
        i = 0
        result = []
        local_result = []
        match_found = False

        for current in array2:
            if i < len(array1) and current == array1[i]:
                if not match_found:
                    match_found = True
                local_result.append(current)
                i += 1
            elif i < len(array1) and current != array1[i] and match_found:
                match_found = False
                if len(local_result) > len(result):
                    result = local_result
                local_result = []
                i = 0
        if match_found:
            if len(local_result) > len(result):
                result = local_result
        return result




my_sol = Solution()

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(my_sol.intersect(nums1, nums2)) #[4,9]

array1 = [1, 2, 2, 1]
array2 = [2, 2]
print(my_sol.intersect(array1, array2)) #[2, 2]
