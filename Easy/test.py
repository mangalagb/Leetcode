class Solution(object):
    def removeDuplicates(self, nums):

        size_of_array = len(nums)
        if size_of_array == 0 or size_of_array == 1:
            return size_of_array

        prev = nums[0]
        position = 1
        for i in range(1, size_of_array):
            if nums[i] > prev:
                nums[position] = nums[i]
                prev = nums[i]
                position += 1



        print(nums)
        print(position)
        return position



my_sol = Solution()
l1 = [1,1,1,2]
l2 = [0,0,1,1,1,2,2,3,3,4]
l3 = [0,0,1,1,2,2]
l4 = [1,2,3,4,5]
l5 = []
l6 = [8]

my_sol.removeDuplicates(l1)
my_sol.removeDuplicates(l2)
my_sol.removeDuplicates(l3)
my_sol.removeDuplicates(l4)
my_sol.removeDuplicates(l5)
my_sol.removeDuplicates(l6)