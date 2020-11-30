# Given a non-empty string s and a dictionary wordDict containing a list
# of non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

#start from the front, try to see if the substring (0,i) is in the dict,
# if so, recursively check if there is a way to break (i, s.length)


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        set_of_indexes = set()
        result = self.do_DFS(s, wordDict, set_of_indexes, 0)
        return result

    def do_DFS(self, s, wordDict, set_of_indexes, index):
        if index == len(s):
            return True

        for i in range(index, len(s)):
            if i in set_of_indexes:
                continue

            new_word = s[index:i+1]
            if self.is_valid_word(new_word, wordDict):
                set_of_indexes.add(i)
                result = self.do_DFS(s, wordDict, set_of_indexes, i+1)
                if result:
                    return True
        return False


    def is_valid_word(self, word, wordDict):
        if word in wordDict:
            return True
        return False

my_sol = Solution()

# s = "leetcode"
# wordDict = ["leet", "code"]
# print(my_sol.wordBreak(s, wordDict)) #True
#
# s = "applepenapple"
# wordDict = ["apple", "pen"]
# print(my_sol.wordBreak(s, wordDict)) #True

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(my_sol.wordBreak(s, wordDict)) #False
