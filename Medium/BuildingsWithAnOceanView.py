#There are n buildings in a line. You are given an integer array heights of size n that represents the
# heights of the buildings in the line.

# The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean
# without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.
#
# Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        number_of_buildings = len(heights)
        if number_of_buildings == 0:
            return []
        elif number_of_buildings == 1:
            return [0]

        max_seen_so_far = None
        result = []
        for i in range(number_of_buildings-1, -1, -1):
            current_building = heights[i]

            if max_seen_so_far is None:
                result.insert(0, i)
                max_seen_so_far = current_building
            else:
                if current_building > max_seen_so_far:
                    result.insert(0, i)
                    max_seen_so_far = current_building

        return result


my_sol = Solution()

heights = [4, 2, 3, 1]
print(my_sol.findBuildings(heights)) #[0,2,3]

heights = [4,3,2,1]
print(my_sol.findBuildings(heights)) #[0,1,2,3]

heights = [1,3,2,4]
print(my_sol.findBuildings(heights)) #[3]


