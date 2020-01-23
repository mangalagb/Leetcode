class Solution:
    def sortColors(self, nums):
        if len(nums) == 0:
            return

        i = 0
        j = len(nums) -1
        one_counters = []

        while i <= j:
            while i <= j and nums[i] == 0:
                if len(one_counters) != 0:
                    index = one_counters.pop(0)
                    nums[index] = 0
                    nums[i] = 1
                else:
                    i += 1

            while i <= j and nums[j] == 2:
                j -= 1

            if i <= j and nums[i] == 1:
                one_counters.append(i)
                i += 1

            if i <= j and nums[i] == 2:
                temp = nums[j]
                nums[j] = 2

                if temp == 0:
                    nums[i] = temp
                else:
                    one_counters.append(i)
                    nums[i] = temp
                    i += 1
        print(nums)

nums = [0,2,0,1,0,2,2,2]
#nums = [2,0,2,1,1,0]
#nums = [2, 0, 1]

print(nums)
my_solution = Solution()
my_solution.sortColors(nums)