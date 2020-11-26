# Given an array of characters, compress it in-place.
#
# The length after compression must always be smaller than or equal to the original array.
#
# Every element of the array should be a character (not int) of length 1.
#
# After you are done modifying the input array in-place, return the new length of the array.

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
