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
        new_ship_capacity = -1
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid_value = (high - low) // 2
            mid = low + mid_value
            capacity_possible = self.is_weight_possible(mid, weights, D)

            if not capacity_possible:
                low = mid + 1
            else:
                new_ship_capacity = mid
                high = mid - 1

        return new_ship_capacity


    def is_weight_possible(self, ship_capacity, weights, D):
        days = 0
        running_weight = 0
        i = 0

        while days < D and i < len(weights):
            while running_weight <= ship_capacity and i < len(weights):
                running_weight += weights[i]
                i += 1

            if running_weight > ship_capacity:
                days += 1
                running_weight = 0
                i -= 1

        if i >= len(weights):
            return True
        else:
            return False


my_sol = Solution()

weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
print(my_sol.shipWithinDays(weights, D))