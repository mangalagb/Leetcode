# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that
# each letter appears in at most one part, and return a list of integers representing the size of these parts.

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        indexes = {S[0]: 0}
        end = 1
        begin = 0
        i = 1

        









my_sol = Solution()

# S = "ababcbacadefegdehijhklij"
# my_sol.partitionLabels(S)
#
# S = "abaccbdeffed"
# my_sol.partitionLabels(S)

S = "abaj"
my_sol.partitionLabels(S)
