# #Given a nested list of integers, return the sum of all integers in the
# list weighted by their depth.
#
# Each element is either an integer, or a list -- whose elements
# may also be integers or other lists.


class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        result = self.get_sum_by_level(nestedList, 1)
        return result

    def get_sum_by_level(self, nums, level):
        result = 0

        for element in nums:
            try:
                len(element)
                is_integer = False
            except:
                is_integer = True

            if is_integer:
                local_sum = element * level
                result += local_sum
            else:
                local_sum = self.get_sum_by_level(element, level+1)
                result += local_sum
        return result



my_sol = Solution()

nums = [[1,1],2,[1,1]]
print(my_sol.depthSum(nums)) #10  Four 1's at depth 2, one 2 at depth 1.

nums = [1,[4,[6]]]
print(my_sol.depthSum(nums)) #27
# One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

nums = [1,[4,[], [], []]]
print(my_sol.depthSum(nums)) #9

nums = [[], [], []]
print(my_sol.depthSum(nums)) #0

nums = [[[[]]]]
print(my_sol.depthSum(nums)) #0

nums = []
print(my_sol.depthSum(nums)) #0

