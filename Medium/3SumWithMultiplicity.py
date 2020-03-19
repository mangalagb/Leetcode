# Given an integer array A, and an integer target, return the number of tuples i, j, k
# such that i < j < k and A[i] + A[j] + A[k] == target.
#
# As the answer can be very large, return it modulo 10^9 + 7.
from collections import defaultdict


class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        length_of_nums = len(A)
        frequencies = defaultdict(int)
        for num in A:
            frequencies[num] += 1

        unique_numbers = set()
        for k in range(0, length_of_nums-1):
            i = k + 1
            j = length_of_nums -1

            while i < j:
                if A[k] + A[i] + A[j] == target:
                    string_num = str(A[k]) + "," + str(A[i]) + "," + str(A[j])
                    if string_num not in unique_numbers:
                        unique_numbers.add(string_num)
                    i += 1
                    j -= 1
                elif A[k] + A[i] + A[j] < target:
                    i += 1
                else:
                    j -= 1

        result = 0
        for tuple in unique_numbers:
            nums = [int(x) for x in tuple.split(",")]
            num1 = nums[0]
            num2 = nums[1]
            num3 = nums[2]
            answer = 1

            if num1 != num2 != num3:
                answer *= self.find_combination(frequencies[num1], 1)
                answer *= self.find_combination(frequencies[num2], 1)
                answer *= self.find_combination(frequencies[num3], 1)

            elif num1 == num2 and num2 != num3:
                answer *= self.find_combination(frequencies[num1], 2)
                answer *= self.find_combination(frequencies[num3], 1)

            elif num2 == num3 and num1 != num2:
                answer *= self.find_combination(frequencies[num2], 2)
                answer *= self.find_combination(frequencies[num1], 1)
            else:
                answer *= self.find_combination(frequencies[num1], 3)

            result += answer

        MOD = 10 ** 9 + 7
        result = result % MOD
        return result

    def find_combination(self, n, r):
        top_ans = self.factorial(n)
        bottom_answer = self.factorial(r) * (self.factorial(n-r))

        answer = top_ans // bottom_answer
        return answer

    def factorial(self, num):
        ans = 1
        while num > 1:
            ans *= num
            num -= 1
        return ans

my_sol = Solution()

A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
target = 8
print(my_sol.threeSumMulti(A, target)) #20

A = [1,1,2,2,2,2]
target = 5
print(my_sol.threeSumMulti(A, target)) #12