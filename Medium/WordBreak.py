class Solution:
    def wordBreak(self, s, wordDict):
        ans = self.find_ans(s, wordDict)
        return ans

    def find_ans(self, str, wordDict):
        if len(str) == 0:
            return True

        contains_words = False

        for i in range(0, len(str)+1):
            word = str[0:i]

            if word in wordDict:
                #new_str = str.replace(word, "", 1)
                new_str = str[i:]
                flag = self.find_ans(new_str, wordDict)
                if flag:
                    contains_words = True
                    break
                else:
                    contains_words = False
        return contains_words



my_sol = Solution()

s = "applepenapple"
wordDict = ["apple", "pen"]
print(my_sol.wordBreak(s, wordDict))

# s = "leetcode"
# wordDict = ["leet", "code"]
# print(my_sol.wordBreak(s, wordDict))
#
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# print(my_sol.wordBreak(s, wordDict))
#
# s = "cars"
# wordDict = ["car","ca","rs"]
# print(my_sol.wordBreak(s, wordDict))
#
# s = "ccbb"
# wordDict = ["bc","cb"]
# print(my_sol.wordBreak(s, wordDict))
#
# s =  "aaaaaaa"
# wordDict = ["aaaa","aaa"]
# print(my_sol.wordBreak(s, wordDict))

# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# print(my_sol.wordBreak(s, wordDict))