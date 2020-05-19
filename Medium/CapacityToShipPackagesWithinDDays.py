# A conveyor belt has packages that must be shipped from one port to another within D days.
#
# The i-th package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on
# the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity
# of the ship.
#
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being
# shipped within D days.

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        print(weights)

my_sol = Solution()

weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
my_sol.shipWithinDays(weights, D)