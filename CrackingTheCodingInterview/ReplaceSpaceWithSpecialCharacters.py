# Write a method to replace all spaces in a string with ‘%20’.

class Solution(object):
    def replaceSpaces(self, word):
        num_of_spaces = 0

        for character in word:
            if character == " ":
                num_of_spaces += 1

        extra_space = 3 * (num_of_spaces-1)
        word_length = len(word)
        result = [1] * (word_length + extra_space)

        counter = 0
        for character in word:
            if character != " ":
                result[counter] = character
                counter += 1
            else:
                result[counter] = "%"
                result[counter+1] = "2"
                result[counter+2] = "0"
                counter += 3
        answer = ''.join(result)
        return answer

my_sol = Solution()

str = "ab da an b"
print(my_sol.replaceSpaces(str))