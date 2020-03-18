# Find the length of the longest substring T of a given string (consists of lowercase letters only) such
# that every character in T appears no less than k times.

class Solution(object):
    # By Stephen pochman
    # If every character appears at least k times, the whole string is ok. Otherwise split by a least frequent
    # character (because it will always be too infrequent and thus can't be part of any ok substring) and
    # make the most out of the splits.
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(z, k) for z in s.split(c))
        return len(s)

    def longestSubstring1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        length_of_string = len(s)
        count = False
        end = 0
        begin = 0
        result = 0
        frequency = {}

        while end < length_of_string:
            current = s[end]

            if current not in frequency:
                frequency[current] = [1, end]
            else:
                frequency[current][0] += 1

            if frequency[current][0] >= k:
                count = True

            end += 1

            while count:
                if not self.all_characters_atleast_k(frequency, k):
                    begin = frequency[current][1]

                if self.verify_all_characters(s[begin:end], k):
                    local_result = end - begin
                    result = max(result, local_result)

                begin_char = s[begin]
                if frequency[begin_char][0] > k:
                    frequency[begin_char][0] -= 1
                    begin += 1

                count = False
        return result

    def all_characters_atleast_k(self, frequency, k):
        values = frequency.values()
        for value in values:
            if value[0] < k:
                return False
        return True

    def verify_all_characters(self, str, k):
        local_map = {}
        for character in str:
            if character in local_map:
                local_map[character] += 1
            else:
                local_map[character] = 1

        values = local_map.values()
        for value in values:
            if value < k:
                return False
        return True

my_sol = Solution()

s = "zzzzzzzzzzaaaaaaaaabbbbbbbbhbhbhbhbhbhbhicbcbcibcbccccccccccbbbbbbbbaaaaaaaaafffaahhhhhiaahiiiiiiiiifeeeeeeeeee"
k = 10
print(my_sol.longestSubstring(s, k)) # 21
#
# s = "aaabb"
# k = 3
# print(my_sol.longestSubstring(s, k)) # 3
#
# s = "ababbc"
# k = 2
# print(my_sol.longestSubstring(s, k)) # 5
#
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
#
# s = "ababss"
# k = 2
# print(my_sol.longestSubstring(s, k)) # 6
#
# s = ""
# k = 2
# print(my_sol.longestSubstring(s, k)) # 0
#
# s = "ababacb"
# k = 3
# print(my_sol.longestSubstring(s, k)) # 0
#
# s = "abbbbbbcaa"
# k = 3
# print(my_sol.longestSubstring(s, k)) # 6

