# Given an array of strings arr. String s is a concatenation of a
# sub-sequence of arr which have unique characters.
#
# Return the maximum possible length of s.

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        if not arr:
            return 0
        elif len(arr) == 1:
            return len(arr[0])

        self.max_length = 0
        self.do_DFS(arr, 0, "")
        return self.max_length

    def do_DFS(self, arr, index, current):
        is_current_unique = self.is_Unique(current)

        if not is_current_unique or index >= len(arr):
            return

        for i in range(index, len(arr)):
            new_str = current + arr[i]
            if self.is_Unique(new_str):
                new_length = len(new_str)
                self.do_DFS(arr, i+1, new_str)
                self.max_length = max(self.max_length, new_length)


    def is_Unique(self, string):
        unique = set()
        for char in string:
            if char in unique:
                return False
            unique.add(char)
        return True

my_sol = Solution()

arr = ["un","iq","ue"]
print(my_sol.maxLength(arr)) #4

arr = ["cha","r","act","ers"]
print(my_sol.maxLength(arr)) #6

arr = ["abcdefghijklmnopqrstuvwxyz"]
print(my_sol.maxLength(arr)) #26
