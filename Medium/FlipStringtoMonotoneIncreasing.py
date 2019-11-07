# A string of '0's and '1's is monotone increasing if it consists of some number
# of '0's (possibly 0), followed by some number of '1's (also possibly 0.)
#
# We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.
#
# Return the minimum number of flips to make S monotone increasing.


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        str_array = list(S)

        #Find number of 1s that come after an index
        number_of_1s = [0] * len(str_array)
        count_number_of_1 = 0

        for i in range(len(str_array)-1, -1, -1):
            number_of_1s[i] = count_number_of_1
            if str_array[i] is "1":
                count_number_of_1 += 1

        # Find number of 0s that come before an index
        number_of_0s = [0] * len(str_array)
        count_number_of_0 = 0

        for i in range(0, len(str_array)):
            number_of_0s[i] = count_number_of_0
            if str_array[i] is "0":
                count_number_of_0 += 1

        #print(number_of_0s)
        #print(number_of_1s)

        N = len(str_array) - 1

        min_flips = -1
        for i in range(0, len(str_array)):
            number_of_flips_before = i - number_of_0s[i]
            number_of_flips_after = (N - i) - number_of_1s[i]
            total_flips = number_of_flips_before + number_of_flips_after

            if min_flips == -1:
                min_flips = total_flips
            elif total_flips < min_flips:
                min_flips = total_flips

        #print(min_flips)
        return min_flips




my_sol = Solution()

# s1 = "00110"
# print(my_sol.minFlipsMonoIncr(s1))
#
# s2 = "010110"
# print(my_sol.minFlipsMonoIncr(s2))
#
# s3 = "00011000"
# print(my_sol.minFlipsMonoIncr(s3))
#
# s4 = "10011111110010111011"
# print(my_sol.minFlipsMonoIncr(s4))
#
# s5 = "101010111001010000011101101110"
# print(my_sol.minFlipsMonoIncr(s5))

s6 = "11111"
print(my_sol.minFlipsMonoIncr(s6))