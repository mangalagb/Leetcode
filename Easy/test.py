# Write an immutable function that merges the following inputs
# into a single list. (Feel free to use the space below or submit a link to your work.)
#
# Inputs
# - Original list of strings
# - List of strings to be added
# - List of strings to be removed
#
# Return
# - List shall only contain unique values
# - List shall be ordered as follows
# --- Most character count to least character count
# --- In the event of a tie, reverse alphabetical
#
# Other Notes
# - You can use any programming language you like
# - The function you submit shall be runnable

class Solution(object):
    def order_list(self, original_strings, added_strings, removed_strings):
        new_list = set(original_strings.copy())

        for word in added_strings:
            new_list.add(word)

        for word in removed_strings:
            if word in new_list:
                new_list.remove(word)

        #sort list by character count
        word_dict = {}
        for word in new_list:
            word_length = len(word)
            if word_length not in word_dict:
                word_dict[word_length] = [word]
            else:
                word_dict[word_length].append(word)

        result = []
        for key in sorted(word_dict, reverse=True):
            values = word_dict[key]
            if len(values) < 2:
                result.append(values[0])
            else:
                reversed_alphabetical = sorted(values, reverse=True)
                result.extend(reversed_alphabetical)
        return result





# my_sol = Solution()
#
# OriginalList = ['one', 'two', 'three',]
# AddList = ['one', 'two', 'five', 'six']
# DeleteList = ['two', 'five']
# print(my_sol.order_list(OriginalList, AddList, DeleteList))
