#Given four integer arrays nums1, nums2, nums3, and nums4 all of
# length n, return the number of tuples (i, j, k, l) such that:
#
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count = 0
        #Add numbers from first 2 arrays and strore their count in a dict
        nums_dict = {}
        for i in nums1:
            for j in nums2:
                total = i + j
                if total in nums_dict:
                    nums_dict[total] += 1
                else:
                    nums_dict[total] = 1

        #The remaining 2 numbers must total - num3 - num4 = 0
        for i in nums3:
            for j in nums4:
                current_sum = i + j
                complement = 0 - current_sum
                if complement in nums_dict:
                    count += nums_dict[complement]
        return count


my_sol = Solution()

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(my_sol.fourSumCount(nums1, nums2, nums3, nums4)) #2

nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]
print(my_sol.fourSumCount(nums1, nums2, nums3, nums4)) #1
