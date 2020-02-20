# Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].
# The width of such a ramp is j - i.
# Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

class Solution(object):
    # Not exactly “find” for every index, rather consider.The problem is to find maximum of all
    # such distances, so trick is that for many indices, we can eliminate that calculation.
    #
    # For [6,0,8,2,1,5]
    # when I know that for 0, right end of the ramp (let’s call it idx2) is 5, I needn’t calculate it for numbers occurring
    # between 0 and 5 for the case of idx2=5, since their distance to 5 would anyways be less than the one between 0 to 5.

    #Classical two pointer problem. Right pointer expands the range and left pointer contracts it. The trick is that
    # left pointer iterates over original array and right pointer iterates over an array which stores maximum no.
    # on the right for each index.

    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length_of_nums = len(A)
        j = length_of_nums - 1
        max_element_on_the_right = [0] * length_of_nums
        max_element_on_the_right[j] = A[j]

        for i in range(length_of_nums-2, -1, -1):
            number = A[i]
            maximum_number = max(number, max_element_on_the_right[i+1])
            max_element_on_the_right[i] = maximum_number

        left = 0
        right = 0
        answer = 0

        while right < length_of_nums:
            while left < right and A[left] > max_element_on_the_right[right]:
                left += 1

            local_ans = right - left
            answer = max(answer, local_ans)
            right += 1
        return answer

    # STACK BASED APPROACH
    # For [6,0,8,2,1,5]
    # Decreasing order stack : 6,0.
    # There’s no point of adding 8 to stack.
    # Since for any element on the right for which 8 would be a part of solution (i.e. 8 is on the left end of ramp),
    #  0 can also be the left end for that ramp and provides a larger length of ramp since index of 0 is less than that
    #  of 8. This assures as that 8 will never be the left end of our largest ramp.
    # Similar explanation applies for 2,1 and 5.

    #Now after we have stack, start iterating the array from end considering :
    # Current element to be the right end of ramp and top element of the stack to be left end of the ramp.
    # If stack’s top element satisfies the condition, we have a candidate ramp.
    #
    # The trick here is: Now we can pop that element out of the stack. Why?
    # Let’s say we were right now at index j of the array and stack’s top is at index i.
    #
    # So ramp is i..j.
    #
    # As we are iterating backwards in the array, the next possible right end of the ramp will be j-1. Even if
    # formes a ramp with i, it’s length would be shorter than our current ramp (i.e. j-i).
    #
    # So, no point in keeping in 0 in stack now.
    #
    # Keep popping elements off the stack whenever we have a candidate ramp. Since the current candidate ramp
    # is the best ramp considering the stack’s top element to the left end of that ramp

    def maxWidthRampStack(self, A):
        stack = []
        length_of_nums = len(A)

        for i in range(0, length_of_nums):
            length_of_stack = len(stack) - 1
            if length_of_stack == -1 or A[i] < stack[length_of_stack]:
                stack.append(A[i])

        answer = 0
        length_of_stack = len(stack) - 1
        for j in range(length_of_nums-1, -1, -1):
            while length_of_stack >= 0 and A[j] > stack[length_of_stack]:
                answer = max((j - stack.pop(length_of_stack)), answer)
                length_of_stack = len(stack) - 1

        return answer



my_sol = Solution()

nums = [6,0,8,2,1,5]
print(my_sol.maxWidthRamp(nums))

nums = [9,8,1,0,1,9,4,0,4,1]
print(my_sol.maxWidthRamp(nums))
#
# nums = [2,3,1]
# print(my_sol.maxWidthRamp(nums))
#
# nums = [9,27,14,25,25,21,23,22,20,20,19,18,18,19,10,11,10,8,8,8,0,28,6,6,5,9,2,2,2,0]
# print(my_sol.maxWidthRamp(nums))

# nums = [6,0,8,2,1,5]
# print(my_sol.maxWidthRampStack(nums))
#
# nums = [9,8,1,0,1,9,4,0,4,1]
# print(my_sol.maxWidthRampStack(nums))