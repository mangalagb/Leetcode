# Given a non-negative integer, you could swap two digits at
# most once to get the maximum valued number. Return the maximum valued number you could get.

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        number = [int(x) for x in str(num)]

        modified = False
        max_index = -1
        while not modified:
            remaining_num = number[max_index+1:]
            if len(remaining_num) == 0:
                break

            max_num, local_index = self.find_max(remaining_num)
            max_index = max_index + local_index + 1
            i = 0
            if max_index != -1:
                while i < len(number):
                    current = number[i]
                    if current < max_num and i < max_index:
                        number[i] = max_num
                        number[max_index] = current
                        modified = True
                        break
                    i += 1

        result = 0
        for i in range(0, len(number)):
            result = (10 * result) + number[i]
        return result

    def find_max(self,  number):
        max_num = -1
        max_index = -1
        for i in range(len(number) - 1, -1, -1):
            digit = number[i]
            if digit > max_num:
                max_num = digit
                max_index = i
            if digit == 9:
                break
        return max_num,max_index



my_sol = Solution()

number = 99901
print(my_sol.maximumSwap(number)) #99910

number = 2736
print(my_sol.maximumSwap(number)) #7236

number = 2
print(my_sol.maximumSwap(number)) #2

number = 9973
print(my_sol.maximumSwap(number)) #9973

number = 2979
print(my_sol.maximumSwap(number)) #9972

number = 2970089
print(my_sol.maximumSwap(number)) #9970082

number = 297008
print(my_sol.maximumSwap(number)) #927008

number = 0
print(my_sol.maximumSwap(number)) #0

number = 98368
print(my_sol.maximumSwap(number))#98863
