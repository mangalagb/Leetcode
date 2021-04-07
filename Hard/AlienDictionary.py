# #There is a new alien language that uses the English alphabet. However, the order
# among letters are unknown to you.
#
# You are given a list of strings words from the dictionary, where words are sorted
# lexicographically by the rules of this new language.
#
# Derive the order of letters in this language, and return it. If the given input is
# invalid, return "". If there are multiple valid solutions, return any of them.

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) == 1:
            return words[0]

        adj_list = self.make_graph(words)
        if adj_list is None:
            return ""
        self.top_sort = []

        visited = set()
        temp_visited = set()

        #Do topological sort
        for key in adj_list.keys():
            result = self.do_top_sort(key, visited, temp_visited, adj_list)
            if not result:
                return ""

            if len(self.top_sort) == len(adj_list):
                break

        if len(self.top_sort) != len(adj_list):
            return ""

        result = ''.join(self.top_sort)
        return result

    def do_top_sort(self, node, visited, temp_visited, adj_list):
        if node in visited:
            return True

        if node in temp_visited:
            return False

        temp_visited.add(node)

        for child in adj_list[node]:
            result = self.do_top_sort(child, visited, temp_visited, adj_list)
            if not result:
                return False

        temp_visited.remove(node)
        visited.add(node)

        self.top_sort.insert(0, node)
        return True


    def make_graph(self, words):
        adj_list = {}

        word1 = words[0]
        for character in word1:
            if character not in adj_list:
                adj_list[character] = []

        for i in range(1, len(words)):
            word2 = words[i]

            first, second = self.find_order(word1, word2)
            #ADD common characters to adj list
            for character in word2:
                if character not in adj_list:
                    adj_list[character] = []

            # words like "abc" and "abc" are already sorted
            if first is None:
                return None
            elif second is None:
                adj_list[first] = []

            else:
                #Second comes after first in orderind
                # A -> B
                if first not in adj_list:
                    adj_list[first] = [second]
                else:
                    adj_list[first].append(second)

                #Add second to adj_list
                if second not in adj_list:
                    adj_list[second] = []

            word1 = word2
        return adj_list

    def find_order(self, word1, word2):
        i = 0
        first_letter = word1[0]
        second_letter = word2[0]

        while i < len(word1) and i < len(word2):
            char1 = word1[i]
            char2 = word2[i]

            if char1 != char2:
                first_letter = char1
                second_letter = char2
                break
            i += 1

        if first_letter == second_letter and len(word1) > i:
            return None, None
        elif first_letter == second_letter:
            return first_letter, None
        else:
            return first_letter, second_letter


my_sol = Solution()

words = ["abc","ab"]
print(my_sol.alienOrder(words)) #""

words = ["wrt","wrtkj"]
print(my_sol.alienOrder(words)) #"jkrtw"

words = ["ab","adc"]
print(my_sol.alienOrder(words)) #"abcd"

words = ["z","z"]
print(my_sol.alienOrder(words)) #z

words = ["wrt","wrf","er","ett","rftt"]
print(my_sol.alienOrder(words)) #"wertf", werft

words = ["z","x","z"]
print(my_sol.alienOrder(words)) #""

words = ["z","x"]
print(my_sol.alienOrder(words)) #"zx"

words = ["zy","zx"]
print(my_sol.alienOrder(words)) #"yxz"

