# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is "":
            return True

        word = []
        for character in s:
            if character.isalnum():
                word.append(character.lower())

        i = 0
        j = len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True


my_sol = Solution()

s = "A man, a plan, a canal: Panama"
print(my_sol.isPalindrome(s)) #True

s = "race a car"
print(my_sol.isPalindrome(s)) #False
