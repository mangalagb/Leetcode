#Given a string, find the length of the longest substring without repeating
#characters.

# Window method

class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        characters = {}
        count = 0
        local_count = 0
        repeated_index = -1

        for i in range(0, len(s)):
            if s[i] not in characters:
                local_count += 1
                characters[s[i]] = i

            else:
                #Get the previous element's index from the hashmap
                index = characters[s[i]]

                #This happens in the case of say abba
                #If we know element 2 is repeated, then we need not count from
                #  element 0
                if index < repeated_index:
                    characters[s[i]] = i
                    local_count = i - repeated_index
                else:
                    #The running count will be current index-index of last repeated
                    local_count = i - index

                    #Update the hashmap to the current repeated element index
                    characters[s[i]] = i

                    #store the index where this value was changed
                    repeated_index = index

            if local_count > count:
                count = local_count

        return count






str1 = "abcabcbb"
str2 = "bbbbb"
str3 = "pwwkew"
str4 = "aab"
str5 = "au"

str6 = "dvdf"
str7 = "abba"

my_str = ["abcabcbb", "bbbbb", "pwwkew", "aab", "au", "dvdf", "abba", "tmmzuxt"]


my_solution = Solution()
# for strs in my_str:
#     print(my_solution.lengthOfLongestSubstring(strs))

my_solution.lengthOfLongestSubstring(str1)
