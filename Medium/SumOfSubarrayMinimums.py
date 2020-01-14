class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #sum_of_subarray_minimum %= 1000000007
        #self.print_subarrays(0, 0, A)
        my_list = [0, 0]
        result = self.print_subarrays(A, my_list)
        # total_sum = result[1] % 1000000007
        # print(total_sum)
        # return total_sum

        total_sum = result[1]
        print(total_sum)
        return total_sum

    def print_subarrays(self, A, my_list):
        if len(A) == 1:
            min_so_far = A[0]
            rolling_sum = A[0]
            return [min_so_far, rolling_sum]

        length_of_array = len(A) - 1

        last_element = A[length_of_array]
        new_array = A[:length_of_array]
        subarray_result = self.print_subarrays(new_array, my_list)

        #Add the individual element to rolling sum
        rolling_sum = subarray_result[1]
        rolling_sum += last_element

        min_so_far = min(subarray_result[0], last_element)
        rolling_sum += min_so_far
        local_result = [min_so_far, rolling_sum]
        return local_result

my_sol = Solution()

a1 = [3,1,2,4] #17
a2 = [81,55,2] #197
a3 = [62,92,97] #467
a4 = [71,55,82,55]  #593
a5 = [19,19,62,66] #323
a6 = [85,93,93,90] #889
a7 = [3, 4, 5] #22
#[3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].

#my_sol.sumSubarrayMins(a1)
# my_sol.sumSubarrayMins(a2)
# my_sol.sumSubarrayMins(a3)
# my_sol.sumSubarrayMins(a4)
# my_sol.sumSubarrayMins(a5)
# my_sol.sumSubarrayMins(a6)
my_sol.sumSubarrayMins(a7)
