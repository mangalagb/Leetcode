class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        [num, index] = self.find_closest(arr, x)
        result = self.find_k_elements(arr, k, num, index)
        return result

    def find_closest(self, elements, x):
        high = len(elements) - 1
        low = 0
        result = None

        while low <= high:
            mid = (high - low) // 2
            result = [elements[mid], mid]

            if elements[mid] == x:
                return [x, mid]

            diff = x - elements[mid]
            if diff < 0:
                high = mid - 1
            elif diff > 0:
                low = mid + 1
        return result

    def find_k_elements(self, elements, k, num, index):
        count = 1
        left_index = index - 1
        right_index = index + 1
        result = [elements[index]]

        while count < k:
            left_num = None
            right_num = None
            count += 1

            if left_index >= 0:
                left_num = elements[left_index]
            if right_index < len(elements):
                right_num = elements[right_index]

            if left_num and right_num:
                left_diff = num - left_num
                right_diff = right_num - num
                if left_diff <= right_diff:
                    result.insert(0, left_num)
                    left_index -= 1
                elif left_diff > right_diff:
                    result.append(right_num)
                    right_index += 1
            elif left_num:
                result.insert(0, left_num)
                left_index -= 1
            elif right_num:
                result.append(right_num)
                right_index += 1

        return result


my_sol = Solution()

arr = [1, 2, 3, 4, 5]
k = 4
x = 3
print(my_sol.findClosestElements(arr, k, x)) #[1, 2, 3, 4]

arr = [1,2,3,4,5]
k = 4
x = -1
print(my_sol.findClosestElements(arr, k, x)) #[1, 2, 3, 4]
