#In an alien language, surprisingly they also use english
# lowercase letters, but possibly in a different order. The order
# of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the
# order of the alphabet, return true if and only if the given words
# are sorted lexicographicaly in this alien language.

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words) == 1:
            return True

        word1 = words[0]
        for i in range(1, len(words)):
            word2 = words[i]
            is_sorted = self.find_if_sorted(word1, word2, order)
            if not is_sorted:
                return False
            word1 = word2
        return True

    def find_if_sorted(self, word1, word2, order):
        word1, word2 = self.make_same_length(word1, word2)
        order = "." + order

        for i in range(0, len(word1)):
            char1 = word1[i]
            char2 = word2[i]

            index1 = order.index(char1)
            index2 = order.index(char2)

            if index1 < index2:
                return True
            elif index1 > index2:
                return False
        return True


    def make_same_length(self, word1, word2):
        word1_length = len(word1)
        word2_length = len(word2)

        difference_in_length = word1_length - word2_length
        if difference_in_length > 0:
            word2 = self.fill_with_dots(word2, difference_in_length)
        elif difference_in_length < 0:
            word1 = self.fill_with_dots(word1, abs(difference_in_length))

        return word1, word2


    def fill_with_dots(self, word, difference):
        for i in range(0, difference):
            word = word + "."
        return word


my_sol = Solution()

words = ["kuvp","q"]
order = "ngxlkthsjuoqcpavbfdermiywz"
print(my_sol.isAlienSorted(words, order)) #True

words = ["hello","hello"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(my_sol.isAlienSorted(words, order)) #True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(my_sol.isAlienSorted(words, order)) #True


words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(my_sol.isAlienSorted(words, order)) #False

words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(my_sol.isAlienSorted(words, order)) #False

