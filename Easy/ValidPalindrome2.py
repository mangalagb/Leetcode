#Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) == 1:
            return True

        result = self.find_if_palindrome(s, 0)
        return result

    def find_if_palindrome(self, s, count):
        i = 0
        j = len(s) - 1

        while i < j:
            start = s[i]
            end = s[j]
            if start == end:
                i += 1
                j -= 1
            else:
                if count > 0:
                    return False
                else:
                    new_str1 = s[i:j]
                    new_str2 = s[i + 1:j + 1]

                    result1 = self.find_if_palindrome(new_str1, count+1)
                    if result1:
                        return True
                    result2 = self.find_if_palindrome(new_str2, count+1)
                    return result2
        return True


my_sol = Solution()

s = "abjjbca"
print(my_sol.validPalindrome(s)) #True

s = "abbca"
print(my_sol.validPalindrome(s)) #True

s = "abc"
print(my_sol.validPalindrome(s)) #False

s = "aba"
print(my_sol.validPalindrome(s)) #True

s = "abca"
print(my_sol.validPalindrome(s)) #True

s = "abdgca"
print(my_sol.validPalindrome(s)) #False

s = "a"
print(my_sol.validPalindrome(s)) #True

s = "ab"
print(my_sol.validPalindrome(s)) #True

s = "abddca"
print(my_sol.validPalindrome(s)) #False
