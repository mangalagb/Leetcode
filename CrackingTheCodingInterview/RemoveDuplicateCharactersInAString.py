# Design an algorithm and write code to remove the duplicate characters in a string
# without using any additional buffer. NOTE: One or two additional variables are fine.
# An extra copy of the array is not.

# FOLLOW UP
# Write the test cases for this method.

class Solution(object):
    def removeDuplicate(self, word):
        if not word:
            return

        sorted_word = sorted(word)
        prev = sorted_word[0]
        result = prev
        for i in range(1, len(sorted_word)):
            current = sorted_word[i]

            if current != prev:
                result += current

            prev = current
        return result



my_sol = Solution()

str = "abdaanb"
print(my_sol.removeDuplicate(str))

str = "abababa"
print(my_sol.removeDuplicate(str))
