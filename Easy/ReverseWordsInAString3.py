# Given a string, you need to reverse the order of characters in each
# word within a sentence while still preserving whitespace and initial word order.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        if len(s) == 1:
            return s

        s = s + " "
        begin = 0
        for i in range(0, len(s)):
            if s[i] == " ":
                end = i
                word_to_reverse = s[begin:end]

                before = s[:begin]
                after = s[end:]

                result = self.reverse_word(word_to_reverse)
                s = before + result + after
                begin = i+1
        s = s[:len(s)-1]
        return s

    def reverse_word(self, word):
        begin = 0
        end = len(word) - 1
        characters = []
        for character in word:
            characters.append(character)

        while begin < end:
            temp = characters[begin]
            characters[begin] = characters[end]
            characters[end] = temp
            begin += 1
            end -= 1

        result = "".join(characters)
        return result



my_sol = Solution()

s = "Let's take LeetCode contest"
print(my_sol.reverseWords(s)) #"s'teL ekat edoCteeL tsetnoc"

s = "abc"
print(my_sol.reverseWords(s)) #cba

s = " "
print(my_sol.reverseWords(s)) #" "

s = "a"
print(my_sol.reverseWords(s)) #"a"
