class Solution:
    def trap(self,height):

        if not height:
            return 0

        length_of_array = len(height) - 1

        left = height[0]
        left_heights = []

        right = height[length_of_array]
        right_heights = []

        for i in range(0, length_of_array+1):

            if height[i] > left:
                left = height[i]
            left_heights.insert(i, left)

            j = length_of_array - i
            if height[j] > right:
                right = height[j]
            right_heights.insert(i, right)
        right_heights.reverse()

        water = 0
        for i in range(0, len(height)):
            current = height[i]
            min_height = min(left_heights[i], right_heights[i])
            current_water = min_height - current
            water += current_water
        return water

my_sol = Solution()

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(my_sol.trap(heights))