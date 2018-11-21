# Given a string s and a non-empty string p, find all the start
# indices of p's anagrams in s.

class Solution:
    def findAnagrams(self, s, p):
        characters = {}
        for char in p:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

        end = 0
        begin = 0
        count = len(characters)
        indexes = []
        length = len(s)

        while end < len(s):

            end_char = s[end]
            if end_char in characters:
                characters[end_char] -= 1
                if characters[end_char] == 0:
                    count -= 1
            end += 1

            while count == 0:

                if end - begin < length:
                    if end - begin == len(p):
                        indexes.append(begin)

                begin_char = s[begin]
                if begin_char in characters:
                    characters[begin_char] += 1
                    if characters[begin_char] > 0:
                        count += 1
                begin += 1
        return indexes











my_solution = Solution()
s = "cbaebabacd"
p = "abc"
print(my_solution.findAnagrams(s, p))

s1 = "abab"
p1 = "a"
print(my_solution.findAnagrams(s1, p1))