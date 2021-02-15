#Write a function to find the longest common prefix string
# amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = self.find_prefix(prefix, strs[i])
        return prefix

    def find_prefix(self, word1, word2):
        common = ""
        i = 0
        while i < len(word1) and i < len(word2):
            char1 = word1[i]
            char2 = word2[i]

            if char1 == char2:
                common = common + char1
            else:
                break
            i += 1
        return common


my_sol = Solution()

strs = ["flower","flow","flight"]
print(my_sol.longestCommonPrefix(strs)) #fl

strs = ["dog","racecar","car"]
print(my_sol.longestCommonPrefix(strs)) #

strs = ["dog","doggy","car"]
print(my_sol.longestCommonPrefix(strs)) #
