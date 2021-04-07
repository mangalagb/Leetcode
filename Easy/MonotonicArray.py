# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].
# An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
#
# Return true if and only if the given array A is monotonic.

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # Check increasing
        stack = []
        monotone_increasing = True
        for num in A:
            if not stack:
                stack.append(num)
            else:
                if num >= stack[-1]:
                    stack.append(num)
                else:
                    monotone_increasing = False
                    break

        if monotone_increasing:
            return True

        stack = []
        for num in A:
            if not stack:
                stack.append(num)
            else:
                if num <= stack[-1]:
                    stack.append(num)
                else:
                    return False
        return True


my_sol = Solution()

nums = [1,2,2,3]
print(my_sol.isMonotonic(nums)) #True

nums = [6,5,4,4]
print(my_sol.isMonotonic(nums)) #True

nums = [1,3,2]
print(my_sol.isMonotonic(nums)) #False

nums = [1,2,4,5]
print(my_sol.isMonotonic(nums)) #True

nums =  [1,1,1]
print(my_sol.isMonotonic(nums)) #True

