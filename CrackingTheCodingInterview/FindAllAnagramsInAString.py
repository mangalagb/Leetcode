# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be
# larger than 20,100.
#
# The order of output does not matter.

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        frequency = {}
        for character in p:
            if character in frequency:
                frequency[character] += 1
            else:
                frequency[character] = 1

        count = len(frequency)
        begin = 0
        end = 0
        result = []

        while end < len(s):
            current = s[end]
            if current in frequency:
                frequency[current] -= 1

                if frequency[current] == 0:
                    count -= 1
            end += 1

            while count == 0:
                if end - begin == len(p):
                    result.append(begin)

                begin_char = s[begin]
                if begin_char in frequency:
                    frequency[begin_char] += 1

                    if frequency[begin_char] > 0:
                        count += 1
                begin += 1
        return result

my_sol = Solution()

s = "cbaebabacd"
p = "abc"
print(my_sol.findAnagrams(s, p))


s = "abab"
p = "ab"
print(my_sol.findAnagrams(s, p))
