#Given a string s, partition s such that every substring of the partition
# is a palindrome. Return all possible palindrome partitioning of s.

#A palindrome string is a string that reads the same backward as forward.

#SOLUTION : https://www.youtube.com/watch?t=0&v=d9F1aO_idyE&feature=youtu.be

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.ans = []
        self.helper(s, [])
        return self.ans

    def helper(self, word, curr_list):
        if len(word) == 0:
            self.ans.append(curr_list)

        for i in range(1, len(word)+1):
            left = word[:i]
            right = word[i:]

            if self.is_palindrome(left):
                copy_list = curr_list.copy()
                copy_list.append(left)
                self.helper(right, copy_list)


    def is_palindrome(self, word):
        i = 0
        j = len(word) - 1

        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True


my_sol = Solution()

s = "aab"
print(my_sol.partition(s)) #[["a","a","b"],["aa","b"]]

# s = "a"
# print(my_sol.partition(s)) #[["a"]]
#
# s = "abba"
# print(my_sol.partition(s)) #[['a', 'b', 'b', 'a'], ['a', 'bb', 'a'], ['abba']]
#
# s = "ab"
# print(my_sol.partition(s)) #[["a","b"]]
#
# s = "bb"
# print(my_sol.partition(s)) #[['b', 'b'], ['bb']]
