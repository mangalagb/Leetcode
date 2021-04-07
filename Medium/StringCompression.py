#Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead be
# stored in the input character array chars. Note that group lengths that are
# 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be:
# ["a","2","b","2","c","3"]
#
#
# Follow up:
# Could you solve it using only O(1) extra space?



class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        size_of_chars = len(chars)
        if size_of_chars == 0 or size_of_chars == 1:
            return size_of_chars

        count = 0
        result = ""
        previous = None

        sorted(chars)

        current = None
        for i in range(0, len(chars)):
            current = chars[i]
            if not previous:
                previous = current
                count += 1
            elif current == previous:
                count += 1
            else:
                result = result + previous
                if count > 1:
                    result = result + str(count)
                count = 1
                previous = current

        if count > 0:
            result = result + current
            if count > 1:
                result = result + str(count)

        i = 0
        for character in result:
            chars[i] = character
            i += 1
        return i


my_sol = Solution()

# str1 = ["a","a","b","b","c","c","c"]
# print(my_sol.compress(str1)) #6

str1 = ["a","b","c","a","b","c"]
print(my_sol.compress(str1)) #6
#
# str2 = ["a"]
# my_sol.compress(str2)
#
# str3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# my_sol.compress(str3)
#
# str4 = ["a","a","a","a","a","b"]
# my_sol.compress(str4)
#
# str5 = ["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b",
#         "b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]
# my_sol.compress(str5)
#
# str6 = ["a","a","a","b","b","a","a"]
# my_sol.compress(str6)

# str7 = ["a","b","c","d","e","f","g","g","g","g","g","g","g","g","g","g","g","g","a","b","c"]
# print(my_sol.compress(str7)) #12
