# #A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList,
# return the number of words in the shortest transformation sequence
# from beginWord to endWord, or 0 if no such sequence exists.
#
import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_dict = set(wordList)
        queue = [beginWord]
        level = -1
        visited = set()

        while len(queue) > 0:
            word = queue.pop(0)
            visited.add(word)

            if word == endWord:
                return level

            neighbours = self.find_neighbours(word, word_dict, visited)
            if len(neighbours) > 0:
                for neighbour in neighbours:
                    if neighbour not in queue:
                        queue.append(neighbour)

            level += 1
        return 0

    def find_neighbours(self, word, word_dict, visited):
        alphabets = string.ascii_lowercase
        result = set()

        for i in range(0, len(word)):
            for alphabet in alphabets:
                new_word = word[:i] + alphabet + word[i+1:]
                if new_word in word_dict and new_word not in visited:
                    result.add(new_word)
        return result




my_sol = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(my_sol.ladderLength(beginWord, endWord, wordList)) #5

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
print(my_sol.ladderLength(beginWord, endWord, wordList)) #0
