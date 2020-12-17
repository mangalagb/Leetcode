#Given a string S of lowercase letters, a duplicate removal
# consists of choosing two adjacent and equal letters, and removing them.
#
# We repeatedly make duplicate removals on S until we no longer can.
#
# Return the final string after all such duplicate removals have
# been made.  It is guaranteed the answer is unique.

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S or len(S) == 1:
            return S

        previous = None
        begin = None

        i = 0
        duplicate_present = False
        while i < len(S):
            current = S[i]
            if not previous:
                previous = current
                i += 1
                continue

            while current is previous:
                duplicate_present = True
                if not begin:
                    begin = i
                i += 1

            if duplicate_present:
                end = i-1
                S = self.remove_duplicate(begin, end, S)
                i = -1
            else:
                previous = current
        i += 1


    def remove_duplicate(self, begin, end, S):
        before = S[:begin]
        after = S[end+1:]
        result = before + after
        return result




my_sol = Solution()

S = "abbaca"
print(my_sol.removeDuplicates(S)) #ca
