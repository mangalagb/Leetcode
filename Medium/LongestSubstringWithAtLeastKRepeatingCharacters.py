# Find the length of the longest substring T of a given string (consists of lowercase letters only) such
# that every character in T appears no less than k times.
from collections import defaultdict


class Solution(object):
    def longestSubstring1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        length_of_string = len(s)
        count = False
        end_index = -1
        end = 0
        begin = 0
        result = 0
        frequency = {}

        while end < length_of_string:
            current = s[end]

            if current not in frequency:
                frequency[current] = 1
            else:
                frequency[current] += 1

            if frequency[current] >= 0:
                count = True

            end += 1

            while count:
                begin_char = s[begin]

                frequency[begin_char] -= 1
                







    def longestSubstring1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        length_of_string = len(s)
        count = False
        end_index = -1
        end = 0
        begin = 0
        result = 0
        frequency = {}


        while end < length_of_string:
            current = s[end]

            if current not in frequency:
                frequency[current] = [1, end]
                count = False
            else:
                frequency[current][0] += 1

            if frequency[current][0] >= k:
                count = True

            end += 1

            if count:
                begin = frequency[current][1]

                if end_index != -1 and (begin_index < begin < end_index):
                    begin = begin_index

                local_count = end - begin
                result = max(result, local_count)
                end_index = end - 1
                begin_index = begin

        return result



my_sol = Solution()

# s = "aaabb"
# k = 3
# print(my_sol.longestSubstring(s, k)) # 3
#
# s = "ababbc"
# k = 2
# print(my_sol.longestSubstring(s, k)) # 5

# s = "absccst"
# k = 2
# print(my_sol.longestSubstring(s, k)) # 4
#
# s = "aacdfbb"
# k = 2
# print(my_sol.longestSubstring(s, k)) # 2
#
# s = "abcfyu"
# k = 2
# print(my_sol.longestSubstring(s, k)) # 0
#
# s = "abc"
# k = 1
# print(my_sol.longestSubstring(s, k)) # 3

s = "ababss"
k = 2
print(my_sol.longestSubstring(s, k)) # 6
