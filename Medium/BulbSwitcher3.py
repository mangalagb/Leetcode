#There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to
# right. Initially, all the bulbs are turned off.

# At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change
# color to blue only if it is on and all the previous bulbs (to the left) are turned on too.
#
# Return the number of moments in which all turned on bulbs are blue.

class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        running_sum = 0
        count = 0
        largest_n = -1
        sum_if_all_bulbs_are_blue = -1

        for n in light:
            running_sum += n
            if n > largest_n:
                largest_n = n
                sum_if_all_bulbs_are_blue = (largest_n*(largest_n+1)) / 2

            if sum_if_all_bulbs_are_blue <= running_sum:
                count += 1
        return count



my_sol = Solution()

light = [2,1,3,5,4]
print(my_sol.numTimesAllBlue(light)) #3

light = [3,2,4,1,5]
print(my_sol.numTimesAllBlue(light)) #2

light = [4,1,2,3]
print(my_sol.numTimesAllBlue(light)) #1

light = [2,1,4,3,6,5]
print(my_sol.numTimesAllBlue(light)) #3

light = [1,2,3,4,5,6]
print(my_sol.numTimesAllBlue(light)) #6


