#https://medium.com/leetcode-patterns/leetcode-pattern-2-sliding-windows-for-strings-e19af105316b

#Given a string S and a string T, find the minimum window in S which
# will contain all the characters in T in complexity O(n).

class Solution:
    def minWindow(self, S, T):

        # Map to store all characters frequency in substring
        characters = {}
        for char in T:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

        # initialize sliding window
        begin = 0
        end = 0
        count = len(characters)
        ans = ""
        length = len(S)

        # start sliding window
        while end < len(S):
            char = S[end]

            # if current char found in table, decrement count
            if char in characters:
                characters[char] -= 1
                if characters[char] == 0:
                    count -= 1
            end += 1

            # if counter == 0, means we found an answer, now try to
            # trim that window by sliding begin to right.
            while count == 0:
                # store new answer if smaller than previously best
                if end - begin <= length:
                    length = end - begin
                    ans = S[begin:end]


                #begin char could be in table or not,
                # if not then good for us, it was a wasteful char and we
                # shortened the previously found substring.

                # if found in table increment count in table, as we are leaving
                # it out of window and moving ahead
                # so it would no longer be a part of the substring marked by
                # begin-end window

                # table only has count of chars required to make the
                # present substring a valid candidate
                # if the count goes above zero means that the current window
                # is missing one char to be an answer candidate
                new_char = S[begin]
                if new_char in characters:
                    characters[new_char] += 1
                    if characters[new_char] > 0:
                        count += 1
                begin += 1
        return ans

mySolution = Solution()
S = "ADOBECODEBANC"
T = "ABC"
print(mySolution.minWindow(S, T))
