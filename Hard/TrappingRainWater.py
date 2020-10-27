# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

# #public int trap(int[] height) {
#         if (height == null || height.length < 2) return 0;
#
#         Stack<Integer> stack = new Stack<>();
#         int water = 0, i = 0;
#         while (i < height.length) {
#             if (stack.isEmpty() || height[i] <= height[stack.peek()]) {
#                 stack.push(i++);
#             } else {
#                 int pre = stack.pop();
#                 if (!stack.isEmpty()) {
#                     // find the smaller height between the two sides
#                     int minHeight = Math.min(height[stack.peek()], height[i]);
#                     // calculate the area
#                     water += (minHeight - height[pre]) * (i - stack.peek() - 1);
#                 }
#             }
#         }
#         return water;
#     }

class Solution:
    def trap(self,height):
        if not height:
            return 0

        i = 1
        stack = []
        total_water = 0

        while i < len(height):
            current = height[i]
            water = 0

            # Insert current index
            if len(stack) == 0 or current <= height[stack[0]]:
                stack.insert(0, i)

            else:
                popped_index = stack.pop(0)
                popped_element = height[popped_index]

                min_height = min(current, popped_element)
                width = i - popped_index + 1
                water = min_height * width
                total_water += water
            i += 1

        return total_water




my_sol = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]  #6
print(my_sol.trap(height))
#
# height = [4,2,0,3,2,5] #9
# print(my_sol.trap(heights))