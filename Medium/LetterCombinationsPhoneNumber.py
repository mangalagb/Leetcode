class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        alphabets = self.get_mappings()
        final_result = []

        for digit in digits:
            letters = alphabets.get(digit)
            result = final_result.copy()
            final_result.clear()
            for letter in letters:
                local_result = self.get_combinations(letter, result)
                for values in local_result:
                    final_result.append(values)
        return final_result

    def get_combinations(self, letter, combinations):
        if len(combinations) == 0:
            return [letter]
        else:
            temp_result = []
            for combination in combinations:
                temp_result.append(combination + letter)
            return temp_result


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


