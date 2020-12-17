#Given two lists of closed intervals, each list of intervals is
# pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.
#
# (Formally, a closed interval [a, b] (with a <= b) denotes the set
# of real numbers x with a <= x <= b.  The intersection of two closed
# intervals is a set of real numbers that is either empty, or can be
# represented as a closed interval.  For example, the intersection of
# [1, 3] and [2, 4] is [2, 3].)

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A and not B:
            return []
        elif not A:
            return []
        elif not B:
            return []

        i = 0
        j = 0
        result = []

        while i < len(A) and j < len(B):
            first = A[i]
            s1 = first[0]
            e1 = first[1]

            second = B[j]
            s2 = second[0]
            e2 = second[1]

            if (e2 >= s1 and e1 >= s2) or (e1 >= s2 and e2 >= s1):
                new_start = max(s1, s2)
                new_end = min(e1, e2)
                result.append([new_start, new_end])

            #Find if first or second has a larger range
            #If first is [2,5] and second is [3, 10] then increment first
            #There may be more elements matching with second
            if e1 > e2:
                j += 1
            else:
                i += 1
        return result



my_sol = Solution()

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(my_sol.intervalIntersection(A, B)) #[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

A = [[0,2],[5,10],[13,23],[65,80]]
B = [[1,50],[60,100]]
print(my_sol.intervalIntersection(A, B)) #[[1, 2], [5, 10], [13, 23], [65, 80]]

A = [[0,4],[7,8],[12,19]]
B = [[0,10],[14,15],[18,20]]
print(my_sol.intervalIntersection(A, B)) #[[0,4],[7,8],[14,15],[18,19]]
