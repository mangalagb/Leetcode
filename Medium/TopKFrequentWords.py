# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then
# the word with the lower alphabetical order comes first.

from collections import defaultdict

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        frequency = defaultdict(int)

        for word in words:
            frequency[word] += 1

        sorted_dict = [v[0] for v in sorted(frequency.items(), key=lambda kv: (-kv[1], kv[0]))]
        result = sorted_dict[:k]
        return result


my_sol = Solution()

words = ["love", "coding", "i", "love", "leetcode", "i"]
k = 2
print(my_sol.topKFrequent(words, k))

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(my_sol.topKFrequent(words, k))
