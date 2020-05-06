#In an array A of 0s and 1s, how many non-empty subarrays have sum S?

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        begin = -1
        end = 0
        current_sum = 0
        count = 0
        length_of_array = len(A)
        array_end_reached = False

        while begin != end:
            if not array_end_reached and end < length_of_array:
                current = A[end]
                current_sum += current

                if end +1 == length_of_array:
                    array_end_reached = True

            if current_sum == S:
                count += 1
                end += 1

            elif current_sum < S:
                end += 1
            elif current_sum > S:
                begin += 1
                begin_num = A[begin]
                current_sum -= begin_num

                if current_sum == S:
                    count += 1
        return count





my_sol = Solution()

A = [1,0,1,0,1]
S = 2
print(my_sol.numSubarraysWithSum(A, S)) #4
#
# A = [1,0,0,0,1]
# S = 2
# print(my_sol.numSubarraysWithSum(A, S)) #1
#
# A = [0,0,0,0,0]
# S = 2
# print(my_sol.numSubarraysWithSum(A, S)) #0
#
# A = []
# S = 2
# print(my_sol.numSubarraysWithSum(A, S)) #0

# A = [0,0,0,0,0]
# S = 0
# print(my_sol.numSubarraysWithSum(A, S)) #15
