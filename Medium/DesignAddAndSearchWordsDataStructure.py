# Design a data structure that supports adding new words and
# finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data
# structure that matches word or false otherwise. word may contain
# dots '.' where dots can be matched with any letter.
import collections


class Node(object):
    def __init__(self, value=None):
        self.children_dict = {}
        self.isWord = False
        self.value = value

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(-1)


    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for character in word:
            if character in current.children_dict:
                current = current.children_dict[character]
            else:
                new_node = Node(character)
                current.children_dict[character] = new_node
                current = new_node
        current.isWord = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        self.res = False
        self.do_DFS(node, word)
        return self.res


    def do_DFS(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return
        if word[0] == ".":
            for n in node.children_dict.values():
                self.do_DFS(n, word[1:])
        else:
            if word[0] not in node.children_dict:
                return

            node = node.children_dict[word[0]]
            if not node:
                return
            self.do_DFS(node, word[1:])


wordDictionary = WordDictionary()
# wordDictionary.addWord("bad")
# wordDictionary.addWord("dad")
# wordDictionary.addWord("mad")
# print(wordDictionary.search("pad"))# False
# print(wordDictionary.search("bad"))# True
# print(wordDictionary.search(".ad"))# True
# print(wordDictionary.search("b.."))#True
#
# print(wordDictionary.search("."))#False
# print(wordDictionary.search("..."))#True
# print(wordDictionary.search("badd"))#False
# print(wordDictionary.search(".a."))#True


wordDictionary.addWord("at")
wordDictionary.addWord("and")
wordDictionary.addWord("an")
wordDictionary.addWord("add")

print(wordDictionary.search("a"))# False
print(wordDictionary.search(".at"))# False

wordDictionary.addWord("bat")

print(wordDictionary.search(".at"))# True
print(wordDictionary.search("an."))# True
print(wordDictionary.search("a.d."))#False

print(wordDictionary.search("b."))#False
print(wordDictionary.search("a.d"))#True
print(wordDictionary.search("."))#False
