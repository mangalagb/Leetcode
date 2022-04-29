#Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.find_permutations(nums, 0, len(nums)-1)
        return self.result

    def find_permutations(self, numbers, left, right):
        if left == right:
            self.result.append(numbers)
        else:
            for i in range(left, right + 1):
                #Create a deep copy of numbers.
                #Otherwise original numbers will be modified
                new_numbers = numbers.copy()

                # Fix the ith number and permute the rest
                #Swap(left, i)
                new_numbers[left], new_numbers[i] = new_numbers[i], new_numbers[left]

                self.find_permutations(new_numbers, left + 1, right)


my_sol = Solution()

nums = [1,2,3]
print(my_sol.permute(nums)) #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# nums = [0, 1]
# print(my_sol.permute(nums)) #[[0,1],[1,0]]
#
# nums = [1]
# print(my_sol.permute(nums)) #[[1]]
