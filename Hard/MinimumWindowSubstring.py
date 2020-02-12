# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

class Solution(object):
    def minWindow(self, S, T):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # initialize frequency table for T
        characters = {}
        for current_char in T:
            if current_char in characters:
                characters[current_char] += 1
            else:
                characters[current_char] = 1

        # initialize sliding window
        begin = 0
        end = 0
        count = len(characters)
        ans = ""
        length = len(S)

        # start sliding window
        while end < len(S):
            current_char = S[end]

            # if current char found in table, decrement count
            if current_char in characters:
                characters[current_char] -= 1
                if characters[current_char] == 0:
                    count -= 1
            end += 1

            # if counter == 0, means we found an answer, now try to trim that window by sliding begin to right.
            while count == 0:
                # store new answer if smaller than previously best
                if end - begin <= length:
                    length = end - begin
                    ans = S[begin:end]

                # begin char could be in table or not,
                # if not then good for us, it was a wasteful char and we shortened the previously found substring.

                # if found in table increment count in table, as we are leaving it out of window and moving ahead,
                # so it would no longer be a part of the substring marked by begin-end window
                # table only has count of chars required to make the present substring a valid candidate
                # if the count goes above zero means that the current window is missing one char to be an answer
                begin_char = S[begin]
                if begin_char in characters:
                    characters[begin_char] += 1
                    if characters[begin_char] > 0:
                        count += 1
                begin += 1
        return ans

my_sol = Solution()

S = "ADOBECODEBANC"
T = "ABC"
print(my_sol.minWindow(S, T))