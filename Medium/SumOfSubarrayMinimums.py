class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size_of_array = len(A)
        sum_of_subarray_minimum = 0

        for window_size in range(1, size_of_array+1):
            sum_of_subarray_minimum += self.calculate_sum(window_size, A)

        sum_of_subarray_minimum %= 1000000007
        print(sum_of_subarray_minimum)
        return sum_of_subarray_minimum

    def calculate_sum(self, window_size, A):
        local_sum = 0
        if window_size == 1:
            local_sum = A[0]

        queue = [A[0]]
        minimum = A[0]

        for i in range(1, len(A)):
            if window_size == 1:
                local_sum += A[i]
                continue

            delta = None
            if len(queue) < window_size:
                queue.append(A[i])
                if A[i] < minimum:
                    minimum = A[i]

                #even after adding another element, if it is less than window size,
                #we need to add more elements
                if len(queue) != window_size:
                    continue

            elif len(queue) == window_size:
                removed_element = queue.pop(0)
                queue.append(A[i])
                if A[i] <= minimum:
                    minimum = A[i]

                elif removed_element == minimum:
                    delta = A[i] - A[i-1]


            if delta:
                local_sum = local_sum + A[i] - delta
            else:
                local_sum += minimum
        return local_sum

my_sol = Solution()

a1 = [3,1,2,4]
a2 = [81,55,2]
a3 = [62,92,97]
a4 = [71,55,82,55]  #593
a5 = [19,19,62,66] #323

# my_sol.sumSubarrayMins(a1)
# my_sol.sumSubarrayMins(a2)
# my_sol.sumSubarrayMins(a3)
#my_sol.sumSubarrayMins(a4)
my_sol.sumSubarrayMins(a5)