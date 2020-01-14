# Median is the middle value in an ordered integer list. If the size of the list is even,
# there is no middle value. So the median is the mean of the two middle value.
# Examples:
#
# [2,3,4] , the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Your job is to output the median array for each window in the original array.

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window_array = nums[:k]
        window_array = sorted(window_array)
        result = []

        window_even = True
        if k % 2 != 0:
            window_even = False

        if window_even:
            even_median_index1 = k // 2
            even_median_index2 = even_median_index1 - 1
            median = (window_array[even_median_index1] + window_array[even_median_index2])/2
            result.append(median)
        else:
            odd_median_index = k//2
            result.append(window_array[odd_median_index])

        i = k
        while i < len(nums):
            removed_index = i-k
            removed_element = nums[removed_index]

            #Find its index in the window
            index_of_removed_element = -1
            for j in range(0, k):
                if window_array[j] == removed_element:
                    index_of_removed_element = j
                    break

            #remove it and slide all remaing elements to left
            window_array[index_of_removed_element] = None
            for j in range(index_of_removed_element+1, k):
                window_array[j-1] = window_array[j]
                window_array[j] = None

            #Add new element the window
            new_element = nums[i]
            index_to_add = k - 1
            for c in range(0, k):
                current = window_array[c]
                if current and new_element < current:
                        index_to_add = c
                        break

            #Add it to the window at the specified index
            next_element = window_array[index_to_add]
            window_array[index_to_add] = new_element
            for c in range(index_to_add+1, k):
                temp = window_array[c]
                window_array[c] = next_element
                next_element = temp

            #Calculate median
            median_number = None
            if window_even:
                median_number = (window_array[even_median_index1] + window_array[even_median_index2]) / 2
            else:
                median_number = window_array[odd_median_index]
            result.append(median_number)
            i += 1
            #print(window_array)
        return result

my_sol = Solution()

# nums = [1,3,-1,-3,5,3,6,7]  #[1,-1,-1,3,5,6]
# k = 3
# print(my_sol.medianSlidingWindow(nums, k))

nums = [1,4,2,3]
k = 4
print(my_sol.medianSlidingWindow(nums, k))