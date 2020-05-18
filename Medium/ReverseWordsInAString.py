#Given an input string, reverse the string word by word.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        result = ""

        for word in reversed(words):
            if word != "":
                temp = word.strip()
                result += temp
                result += " "

        length_of_result = len(result)
        if length_of_result > 0:
            result = result[:length_of_result-1]
        return result



my_sol = Solution()

words = "the sky is blue"
print(my_sol.reverseWords(words))

words = "  hello world!  "
print(my_sol.reverseWords(words))

words = "a good   example"
print(my_sol.reverseWords(words))
