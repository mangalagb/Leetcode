# Given a string S, check if the letters can be rearranged so that two characters that
# are adjacent to each other are not the same.
# If possible, output any possible result.  If not possible, return the empty string.

from heapq import heappush, heappop

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) == 1:
            return S

        char_count = {}
        for character in S:
            if character in char_count:
                char_count[character] += 1
            else:
                char_count[character] = 1

        my_heap = []
        for k,v in char_count.items():
            heappush(my_heap, ((-1 * v), k))

        new_string = []
        last_index = -1
        while my_heap:
            popped_element = heappop(my_heap)
            most_common_char = popped_element[1]
            most_common_char_value = popped_element[0]

            if last_index != -1 and new_string[last_index] is most_common_char:
                if len(my_heap) == 0:
                    return ""

                second_most_common_char_popped = heappop(my_heap)
                second_most_common_char = second_most_common_char_popped[1]
                second_most_common_char_value = second_most_common_char_popped[0]

                new_string.append(second_most_common_char)
                second_most_common_char_value += 1
                heappush(my_heap, popped_element)
                if second_most_common_char_value < 0:
                    heappush(my_heap, (second_most_common_char_value, second_most_common_char))
            else:
                new_string.append(most_common_char)
                most_common_char_value += 1
                if most_common_char_value < 0:
                    heappush(my_heap, (most_common_char_value, most_common_char))

            last_index += 1

        #print(new_string)
        return ''.join(new_string)

my_sol = Solution()

str1 = "aab"
print(my_sol.reorganizeString(str1))
#aba

str1 = "aaab"
print(my_sol.reorganizeString(str1))

str1 = "vvvlo"
print(my_sol.reorganizeString(str1))
#"vlvov"
