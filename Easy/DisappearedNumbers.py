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

