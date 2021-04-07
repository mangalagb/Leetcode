# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the
# lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# https://leetcode.com/problems/next-permutation/discuss/13994/Readable-code-without-confusing-ij-and-with-explanation


class Solution(object):
    def nextPermutation(self, nums):
        index_to_modify = -1
        for j in range(len(nums)-2, -1, -1):
            if nums[j] >= nums[j+1]:
                continue
            else:
                index_to_modify = j
                break

        if index_to_modify != -1:
            index_of_swap_number = -1
            for i in range(len(nums)-1, index_to_modify, -1):
                if nums[i] > nums[index_to_modify]:
                    index_of_swap_number = i
                    break
            #print(index_of_swap_number)

            #Swap these 2 numbers
            temp = nums[index_to_modify]
            nums[index_to_modify] = nums[index_of_swap_number]
            nums[index_of_swap_number] = temp

            #Reverse the remaing list to get the samllest possible remaining
            # digits
            i = index_to_modify + 1
            j = len(nums) -1
            while i <= j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1

        else:
            nums.sort()

        print(nums)
        #return nums


my_sol = Solution()

nums = [1,2,5,3]
print(nums)
my_sol.nextPermutation(nums)
print("\n")

nums = [1,2,3]
print(nums)
my_sol.nextPermutation(nums)
print("\n")

nums = [2,3,1]
print(nums)
my_sol.nextPermutation(nums)
print("\n")

nums = [3,2,1]
print(nums)
my_sol.nextPermutation(nums)
print("\n")

nums = [1,1,5]
print(nums)
my_sol.nextPermutation(nums)
print("\n")