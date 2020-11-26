# Given a string s, return the longest palindromic substring in s.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        elif len(s) == 1:
            return s

        self.max_length = 0
        self.substring = ""

        for i in range(0, len(s)):
            # Will match cbc
            self.expand_from_middle(s, i, i)
            # Will match cbb
            self.expand_from_middle(s, i, i+1)

        return self.substring


    def expand_from_middle(self, string, left, right):
        if not string or left > right:
            return ""

        while left >= 0 and right < len(string) and string[left] == string[right]:
            substr = string[left:right + 1]
            left -= 1
            right += 1

            local_length = len(substr)
            if local_length > self.max_length:
                self.max_length = local_length
                self.substring = substr



my_sol = Solution()

s = "cbb"
print(my_sol.longestPalindrome(s)) #bb

s = "cbc"
print(my_sol.longestPalindrome(s)) #cbc

s = "babad"
print(my_sol.longestPalindrome(s)) #bab, aba

s = "cbbd"
print(my_sol.longestPalindrome(s)) #bb
#
s = "a"
print(my_sol.longestPalindrome(s)) #a

s = "ac"
print(my_sol.longestPalindrome(s)) #a
