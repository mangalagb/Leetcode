# #You are given an integer array bloomDay, an integer m and an integer k.
#
# You want to make m bouquets. To make a bouquet, you need to use k adjacent
# flowers from the garden.
#
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i]
# and then can be used in exactly one bouquet.
#
# Return the minimum number of days you need to wait to be able to make m bouquets
# from the garden. If it is impossible to make m bouquets return -1.

class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        num_of_flowers_required = m * k
        if len(bloomDay) < num_of_flowers_required:
            return -1

        low = 1
        high = max(bloomDay)
        result = -1

        while low <= high:
            mid = (low + (high - low)//2)

            bloomed_flowers = self.get_flowers_bloomed_on_day(bloomDay, mid)
            is_bouquet_possible = self.is_bouquet_possible(bloomed_flowers, m, k)
            if not is_bouquet_possible:
                low = mid + 1
            else:
                result = mid
                high = mid - 1
        return result



    def get_flowers_bloomed_on_day(self, bloomDay, day):
        flowers = []

        for flower in bloomDay:
            if flower <= day:
                flowers.append("x")
            else:
                flowers.append("-")
        return flowers


    def is_bouquet_possible(self, flowers, m, k):
        #[x, _, x, _, x]
        num_of_bouquets = 0
        num_of_flowers = 0

        for flower in flowers:
            if flower == "-":
                num_of_flowers = 0

            else:
                num_of_flowers += 1
                if num_of_flowers == k:
                    num_of_bouquets += 1
                    num_of_flowers = 0

            if num_of_bouquets == m:
                return True
        return False



my_sol = Solution()

bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(my_sol.minDays(bloomDay, m, k)) #3

bloomDay = [1,10,3,10,2]
m = 3
k = 2
print(my_sol.minDays(bloomDay, m, k)) #-1

bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
print(my_sol.minDays(bloomDay, m, k)) #12