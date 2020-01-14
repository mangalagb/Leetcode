# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.

class Solution(object):
    def findDisappearedNumbers(self, nums):

        if not nums:
            return []

        smallest = 1
        largest = len(nums)

        out = [x for x in range(smallest, largest+1)]
        output = set(out)

        for num in nums:
            if num in output:
                output.remove(num)

        return list(output)


my_sol = Solution()
nums = [4,3,2,7,8,2,3,1]
print(my_sol.findDisappearedNumbers(nums))

nums = []
print(my_sol.findDisappearedNumbers(nums))

