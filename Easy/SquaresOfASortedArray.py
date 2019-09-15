# Given an array of integers A sorted in non-decreasing order,
# return an array of the squares of each number, also in sorted
# non-decreasing order.
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        #Time complexity : O(NlogN)
        #Space complexity : O(1) Sort in place
        nums = [num * num for num in A]
        result = sorted(nums)
        print(result)
        return result

    def sortedSquaresAnother(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        #Time complexity : O(N)
        #Space complexity : O(N)
        l = 0
        r = len(A) - 1
        result = []

        while l <= r:
            left = abs(A[l])
            right = abs(A[r])

            if left > right:
                result.append(left * left)
                l += 1
            else:
                result.append(right * right)
                r -= 1

        result.reverse()
        print(result)



my_sol = Solution()

l1 = [-4,-1,0,3,10]
l2 = [-7,-3,2,3,11]

my_sol.sortedSquaresAnother(l1)
my_sol.sortedSquaresAnother(l2)
