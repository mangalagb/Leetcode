# A string of '0's and '1's is monotone increasing if it consists of some number
# of '0's (possibly 0), followed by some number of '1's (also possibly 0.)
#
# We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.
#
# Return the minimum number of flips to make S monotone increasing.

#Skip 0's until we encounter the first 1.
# Keep track of number of 1's in onesCount (Prefix).
# Any 0 that comes after we encounter 1 can be a potential candidate for flip.
# Keep track of it in flipCount.
# If flipCount exceeds oneCount - (Prefix 1's flipped to 0's)
# a. Then we are trying to flip more 0's (suffix) than number of 1's (prefix) we have.
# b. Its better to flip the 1's instead.


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        flip_count = 0
        one_count = 0

        for character in S:
            if character is "0":
                if one_count == 0:
                    continue
                else:
                    #We can flip the 0 to a 1
                    flip_count += 1

            elif character == "1":
                one_count += 1

            # 2 possibilities. Flip bad zeroes to 1
            # Flip all 1s to 0
            flip_count = min(flip_count, one_count)
        return flip_count




my_sol = Solution()

s1 = "00110"
print(my_sol.minFlipsMonoIncr(s1)) #1

s2 = "010110"
print(my_sol.minFlipsMonoIncr(s2)) #2

s3 = "00011000"
print(my_sol.minFlipsMonoIncr(s3)) #2

s4 = "10011111110010111011"
print(my_sol.minFlipsMonoIncr(s4)) #5

s5 = "101010111001010000011101101110"
print(my_sol.minFlipsMonoIncr(s5)) #11

s6 = "11111"
print(my_sol.minFlipsMonoIncr(s6)) #0