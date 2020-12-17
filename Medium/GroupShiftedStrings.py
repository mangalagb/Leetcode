# Given a string, we can "shift" each of its letter to its
# successive letter, for example: "abc" -> "bcd". We can keep "shifting" which
# forms the sequence:
#
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of non-empty strings which contains only lowercase
# alphabets, group all strings that belong to the same shifting sequence.

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        word_dict = {}
        for string in strings:
            code = self.encode(string)
            if code in word_dict:
                word_dict[code].append(string)
            else:
                word_dict[code] = [string]
        return list(word_dict.values())


    def encode(self, string):
        if len(string) == 0:
            return -1
        elif len(string) == 1:
            return 1

        #Just find diffrence between current and previous character
        #ASCII values. %26 is to adjust for a - z
        code = [-1] * len(string)
        for i in range(1, len(string)):
            current = string[i]
            prev = string[i-1]
            code[i] = (ord(current) - ord(prev)) % 26

        return tuple(code)

my_sol = Solution()

letters = ["abc", "bcd", "acef", "xyz", "ba", "az", "a", "z"]
print(my_sol.groupStrings(letters))
#[
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

letters = ["ab","ba"]
print(my_sol.groupStrings(letters)) #[["ba"],["ab"]]

