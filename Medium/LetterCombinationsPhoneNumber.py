class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        letters = self.get_mappings()
        result = [""]

        for digit in digits:
            temp = []
            alphabets = letters[digit]

            for word in result:
                for alphabet in alphabets:
                    new_word = word + alphabet
                    temp.append(new_word)
            result = temp
        return result


    def get_mappings(self):
        letters = {}
        letters["1"] = []
        letters["2"] = ["a", "b", "c"]
        letters["3"] = ["d", "e", "f"]
        letters["4"] = ["g", "h", "i"]
        letters["5"] = ["j", "k", "l"]
        letters["6"] = ["m", "n", "o"]
        letters["7"] = ["p", "q", "r", "s"]
        letters["8"] = ["t", "u", "v"]
        letters["9"] = ["w", "x", "y", "z"]
        return letters


my_solution = Solution()
digits = "23"
print(my_solution.letterCombinations(digits))
#["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


