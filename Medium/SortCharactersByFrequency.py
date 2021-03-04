#Given a string, sort it in decreasing order based on the frequency of characters.

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        character_map = {}
        for character in s:
            if character in character_map:
                character_map[character] += 1
            else:
                character_map[character] = 1

        sorted_dict = sorted(character_map.items(), key=lambda x: x[1], reverse=True)

        result = []
        for item in sorted_dict:
            character = item[0]
            value = int(item[1])

            for i in range(0, value):
                result.append(character)
        ans = "".join(result)
        return ans


my_sol = Solution()

word = "tree"
print(my_sol.frequencySort(word)) #eetr, "eert"

word = "cccaaa"
print(my_sol.frequencySort(word)) #"cccaaa"

word = "Aabb"
print(my_sol.frequencySort(word)) #"bbAa", "bbaA"


