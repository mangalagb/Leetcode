# On the first row, we write a 0. Now in every subsequent row, we look at the previous row and
# replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
#
# Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.)


class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1 and K == 1:
            return 0

        return self.fibonacci(K, N)

    def fibonacci(self, K, N):
        if N == 2 and K == 1:
            return 0
        elif N == 2 and K == 2:
            return 1

        is_even = False
        if K % 2 == 0:
            is_even = True

        new_k = -1
        if is_even:
            new_k = K//2
        else:
            new_k = K//2 + 1

        returned_result = self.fibonacci(new_k, N-1)
        final_result = None

        if returned_result == 0:
            final_result = [0,1]
        else:
            final_result = [1, 0]

        if is_even:
            return final_result[1]
        else:
            return final_result[0]



my_sol = Solution()

N1 = 1
K1 = 1
print(my_sol.kthGrammar(N1, K1))

N1 = 2
K1 = 1
print(my_sol.kthGrammar(N1, K1))

N1 = 2
K1 = 2
print(my_sol.kthGrammar(N1, K1))

N1 = 4
K1 = 5
print(my_sol.kthGrammar(N1, K1))

N1 = 30
K1 = 434991989
print(my_sol.kthGrammar(N1, K1))

N1 = 3
K1 = 2
print(my_sol.kthGrammar(N1, K1))