# Given an array of integers A, find the sum of min(B), where B
# ranges over every (contiguous) subarray of A.
#
# Since the answer may be large, return the answer modulo 10^9 + 7.

class Solution:
    def sumSubarrayMins(self, A):
        sum = 0

        num_stack = []

        for num in A:
            if num_stack:
                top_elements = num_stack[0].copy()
                subarrays = self.split_numbers(top_elements, num)
                subarrays.extend(num_stack)
                num_stack = subarrays
            else:
                num_stack.append([num])

        print(num_stack)

    def split_numbers(self, top_elements, num):
        top_elements.append(num)

        sub = [top_elements[x:] for x in range(0, len(top_elements))]
        #print(sub)
        return sub









my_sol = Solution()

nums = [3,1,2,4]
my_sol.sumSubarrayMins(nums)

#[3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].