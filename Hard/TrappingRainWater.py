# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

class Solution:
    def trap(self,height):
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        total_water = 0

        #[4,2,0,3,2,5]
        while left < right:
            if height[left] > left_max:
                left_max = height[left]

            if height[right] > right_max:
                right_max = height[right]

            # A taller bar exists on left pointer's right side
            # So compute the left bar's height for water
            if left_max < right_max:
                current_water = left_max - height[left]
                left += 1
            else:
                current_water = right_max - height[right]
                right -= 1
            total_water += current_water
        return total_water



my_sol = Solution()

# height = [0,1,0,2,1,0,1,3,2,1,2,1]  #6
# print(my_sol.trap(height))

height = [4,2,0,3,2,5] #9
print(my_sol.trap(height))