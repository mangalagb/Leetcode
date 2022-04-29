#Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat:
            return

        sum_dict = {}

        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                index_sum = i + j
                number = mat[i][j]

                if index_sum not in sum_dict:
                    sum_dict[index_sum] = [number]
                else:
                    sum_dict[index_sum].append(number)

        result = []
        reverse = True
        i = 0
        while i in sum_dict:
            if reverse:
                temp = sum_dict[i]
                temp.reverse()
                result.extend(temp)
                reverse = False
            else:
                result.extend(sum_dict[i])
                reverse = True
            i += 1

        return result




my_sol = Solution()

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(my_sol.findDiagonalOrder(mat)) # [1,2,4,7,5,3,6,8,9]

mat = [[1,2],[3,4]]
print(my_sol.findDiagonalOrder(mat)) # [1,2,3,4]

mat = [[1,2,3,4]]
print(my_sol.findDiagonalOrder(mat)) # [1,2,3,4]

mat = [[1],[2],[3],[4]]
print(my_sol.findDiagonalOrder(mat)) # [1,2,3,4]
