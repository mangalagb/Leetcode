# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
#
#     B.length >= 3
#     There exists some 0 < i < B.length - 1 such that
#     B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
#
# (Note that B could be any subarray of A, including the entire array A.)
#
# Given an array A of integers, return the length of the longest mountain.
#
# Return 0 if there is no mountain.
#SOLUTION
#find peak and stretch, easy to understand, O(2N)

class Solution(object):
    def longestMountain(self, arr):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(arr) < 3:
            return 0

        result = 0
        for i in range(1, len(arr)-1):
            #Peak condtion
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:

                left = i -1
                while left > 0 and arr[left] > arr[left-1]:
                    left -= 1

                right = i + 1
                while right < len(arr)-1 and arr[right] > arr[right+1]:
                    right += 1

                local_result = right - left + 1
                result = max(result, local_result)
        return result


my_sol = Solution()

num1 = [1,4,7,3,2,5]
print(my_sol.longestMountain(num1)) #5 #[1,4,7,3,2]

num1 = [2,3,3,2,0,2]
print(my_sol.longestMountain(num1)) #0

num1 = [2,2,2]
print(my_sol.longestMountain(num1)) #0

num1 = [0,1,2,3,4,5,4,3,2,1,0]
print(my_sol.longestMountain(num1)) # 11

num1 = [0,1,0]
print(my_sol.longestMountain(num1)) #3

num1 = [0,1,2,3,4,5,6,7,8,9]
print(my_sol.longestMountain(num1)) #0

num1 = [875,884,239,731,723,685]
print(my_sol.longestMountain(num1)) #4

