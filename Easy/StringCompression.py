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

        prev = chars[0]
        counter = 1
        position = 1
        size_list = []

        for i in range(1, size_of_chars):
            if chars[i] is prev:
                counter += 1
                chars[position] = counter
            else:
                if counter != 1:
                    position += 1

                chars[position] = chars[i]
                prev = chars[i]
                if i +1 != size_of_chars:
                    position += 1
                counter = 1

        for i in range(position + 1, len(chars)):
            chars[i] = None

        i=0
        while i < position+1:
            if isinstance(chars[i], str) and i+1<size_of_chars and isinstance(chars[i+1], int):
                size_list.append([chars[i], chars[i+1]])
                i += 2
            else:
                size_list.append([chars[i]])
                i += 1

        index = 0
        for item in size_list:
            if len(item) == 2:
                chars[index] = item[0]
                index += 1
                num_str = str(item[1])
                for char in num_str:
                    chars[index] = char
                    index += 1
            else:
                chars[index] = item[0]
                index += 1

        chars = chars[:index]
        print(chars, index)
        return index

my_sol = Solution()

str1 = ["a","a","b","b","c","c","c"]
str2 = ["a"]
str3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
str4 = ["a","a","a","a","a","b"]
str5 = ["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b",
        "b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]
str6 = ["a","a","a","b","b","a","a"]
str7 = ["a","b","c","d","e","f","g","g","g","g","g","g","g","g","g","g","g","g","a","b","c"]

my_sol.compress(str1)
my_sol.compress(str2)
my_sol.compress(str3)
my_sol.compress(str4)
my_sol.compress(str5)
my_sol.compress(str6)
my_sol.compress(str7)