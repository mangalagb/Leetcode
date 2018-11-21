#You are given a string, s, and a list of words, words, that are
# all of the same length. Find all starting indices of substring(s)
# in s that is a concatenation of each word in words exactly once and
#  without any intervening characters.


class Solution:
    def findSubstring(self, s, words):
        if len(words) == 0:
            return []

        characters = {}
        window_count = 0
        end = 0
        word_length = len(words[0])
        begin = 0
        indexes = []
        total_length = 0

        #prepare array
        for word in words:
            window_count += len(word)
            total_length += len(word)
            if word in characters:
                characters[word] += 1
            else:
                characters[word] = 1

        while (end + word_length) < len(s):
            word = s[end:end+word_length]
            end_changed = False
            if word in characters:
                characters[word] -= 1
                end_changed = True
                window_count -= len(word)

            if end_changed:
                end += word_length
            else:
                end += 1

            while window_count == 0:
                if end - begin < len(s):
                    temp = s[begin:end]
                    if begin not in indexes and len(temp) == total_length:
                        indexes.append(begin)
                        begin = end
                        window_count = total_length
                    else:
                        begin += 1

        return indexes

my_solution = Solution()

s = "barfoothefoobarman"
words = ["foo","bar"]
print(my_solution.findSubstring(s, words))


s1 = "wordgoodstudentgoodword",
words1 = ["word","student"]
print(my_solution.findSubstring(s1, words1))

s2 = "wordgoodgoodgoodbestword"
words2 = ["word","good","best","word"]
print(my_solution.findSubstring(s2, words2))

