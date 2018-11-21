class Solution:
    def lengthOfLongestSubstring(self, s):

        end = 0
        begin = 0
        characters = {}
        length = 0
        ans = s

        while end < len(s):

            char = s[end]

            if char in characters and characters[char] >= begin:
                begin = characters[char] + 1
            else:
                characters[char] = end
                end += 1

            if end-begin > length:
                length = end - begin
                ans = s[begin:end]

        print(ans, len(ans))
        return len(ans)

mySolution = Solution()

s1 = "abcabcbb"
mySolution.lengthOfLongestSubstring(s1)

s2 = "bbbb"
mySolution.lengthOfLongestSubstring(s2)

s3 = "pwwkew"
mySolution.lengthOfLongestSubstring(s3)

s4 = "au"
mySolution.lengthOfLongestSubstring(s4)

s5 = " "
mySolution.lengthOfLongestSubstring(s5)

s6 = "dvdf"
mySolution.lengthOfLongestSubstring(s6)

