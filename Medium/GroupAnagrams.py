#Given an array of strings, group anagrams together.

class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}

        for word in strs:
            new_word = ''.join(sorted(word))
            if new_word not in anagrams:
                anagrams[new_word] = [word]
            else:
                original_list = anagrams[new_word]
                original_list.append(word)
                anagrams[new_word] = original_list

        result = []
        for element in anagrams:
            result.append(anagrams[element])
        return result





strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
my_sol = Solution()
print(my_sol.groupAnagrams(strs))
