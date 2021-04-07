# Given two sparse vectors, compute their dot product.
#
# Implement class SparseVector:
#
# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of
# SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should
# store the sparse vector efficiently and compute the dot product
# between two SparseVector.
#
# Follow up: What if only one of the vectors is sparse?

class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.vector_dict = {}
        for i in range(0, len(nums)):
            if nums[i] != 0:
                self.vector_dict[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        min_hash_map = vec.vector_dict
        max_hash_map = self.vector_dict
        if len(self.vector_dict) < len(vec.vector_dict):
            min_hash_map = self.vector_dict
            max_hash_map = vec.vector_dict

        result = 0
        for index2, val2 in min_hash_map.items():
            if index2 in max_hash_map:
                product = val2 * max_hash_map[index2]
                result += product
        return result



nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2)) #8


nums1 = [0,1,0,0,0]
nums2 = [0,0,0,0,2]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2)) #0

nums1 = [0,1,0,0,2,0,0]
nums2 = [1,0,0,0,3,0,4]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2)) #6
