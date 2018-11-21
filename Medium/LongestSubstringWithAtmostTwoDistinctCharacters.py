class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        characters = {}
        count = 0

        begin = 0
        current = 0
        result = ""

        changed_index = -1
        prev_char = None

        while current < len(s):
            current_char = s[current]

            if current_char not in characters and count < 2:
                if characters:
                    changed_index = current
                else:
                    begin = current

                characters[current_char] = current
                count += 1

            if current_char not in characters and count == 2:
                local_result = s[begin:current]
                if len(local_result) > len(result):
                    result = local_result
                    #print(result)

                characters.clear()
                characters[prev_char] = changed_index
                characters[current_char] = current
                count = 2
                begin = changed_index

            if not prev_char:
                prev_char = current_char
            if prev_char != current_char:
                changed_index = current
                prev_char = current_char
            current += 1

        local_result = s[begin:current]
        if len(local_result) > len(result):
            result = local_result

        #print(result)
        #return result
        return len(result)




my_sol = Solution()

str = "ccaabbb"
print(str,my_sol.lengthOfLongestSubstringTwoDistinct(str))

str = "eceba"
print(str,my_sol.lengthOfLongestSubstringTwoDistinct(str))

str = ""
print(str,my_sol.lengthOfLongestSubstringTwoDistinct(str))

str = "aaaaa"
print(str,my_sol.lengthOfLongestSubstringTwoDistinct(str))

str = "abaccc"
print(str, my_sol.lengthOfLongestSubstringTwoDistinct(str))

str = "ababcbcbaaabbdef"
print(str, my_sol.lengthOfLongestSubstringTwoDistinct(str))
