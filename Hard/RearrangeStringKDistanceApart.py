#Given a non-empty string s and an integer k, rearrange the string
# such that the same characters are at least distance k from each other.

# All input strings are given in lowercase letters. If it is not possible
# to rearrange the string, return an empty string "".

import heapq

class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s:
            return ""
        elif k == 0:
            return s

        char_dict = {}
        for character in s:
            if character not in char_dict:
                char_dict[character] = 1
            else:
                char_dict[character] += 1

        my_heap = []
        for key, val in char_dict.items():
            heapq.heappush(my_heap, [-val, key])

        result = [""] * len(s)
        i = 0

        while len(my_heap) > 0:
            popped_items = []
            interval = k

            while len(my_heap) > 0 and interval > 0:
                popped_item = heapq.heappop(my_heap)
                character = popped_item[1]
                value = popped_item[0]

                #Update the char value and mark it to be put back into heap
                value += 1
                popped_items.append(([value, character]))

                #append to result as long as interval is fine
                result[i] = character
                i += 1
                interval -= 1

            for item in popped_items:
                if item[0] < 0:
                    heapq.heappush(my_heap, item)

            if len(my_heap) == 0:
                break

            if interval > 0:
                return ""

        return "".join(result)


my_sol = Solution()

s = "aabbcc"
k = 3
print(my_sol.rearrangeString(s, k)) #"abcabc"

s = "aaabc"
k = 3
print(my_sol.rearrangeString(s, k)) #""

s = "aaadbbcc"
k = 2
print(my_sol.rearrangeString(s, k)) #"abacabcd"
