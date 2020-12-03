#Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
# the x-axis forms a container, such that the container contains the most water.

#Notice that you may not slant the container.

# 1) The widest container (using first and last line) is a good candidate, because of its width.
#   Its water level is the height of the smaller one of first and last line.
# 2) All other containers are less wide and thus would need a higher water level in
#   order to hold more water.
# 3) The smaller one of first and last line doesn't support a higher
#   water level and can thus be safely removed from further consideration.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_area = 0

        while i < j:
            width = j - i
            min_height = min(height[i], height[j])

            area = width * min_height
            max_area = max(max_area, area)

            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return max_area

my_sol = Solution()

height = [1,8,6,2,5,4,8,3,7]
print(my_sol.maxArea(height)) #49

