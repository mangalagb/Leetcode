# Given the string croakOfFrogs, which represents a combination of the
# string "croak" from different frogs, that is, multiple frogs can croak
# at the same time, so multiple “croak” are mixed. Return the minimum number
# of different frogs to finish all the croak in the given string.
#
# A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’
# sequentially. The frogs have to print all five letters to finish a croak.
# If the given string is not a combination of valid "croak" return -1.

class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        frogs = 0
        max_frogs = 0

        frog_dict = {}
        frog_dict["c"] = 0
        frog_dict["r"] = 0
        frog_dict["o"] = 0
        frog_dict["a"] = 0
        frog_dict["k"] = 0

        prev_dict = {}
        prev_dict["r"] = "c"
        prev_dict["o"] = "r"
        prev_dict["a"] = "o"
        prev_dict["k"] = "a"

        for current in croakOfFrogs:
            if current == "c":
                frogs += 1
                max_frogs = max(max_frogs, frogs)

                # Increase count of current letter
                frog_dict[current] += 1

            elif current == "k":
                frogs -= 1
                prev_char = prev_dict[current]
                if frog_dict[prev_char] == 0:
                    return -1
                # Decrease previous character
                frog_dict[prev_char] -= 1

            else:
                prev_char = prev_dict[current]
                if frog_dict[prev_char] == 0:
                    return -1

                #Decrease previous character
                frog_dict[prev_char] -= 1

                # Increase count of current letter
                frog_dict[current] += 1

        for key, value in frog_dict.items():
            if value > 0:
                return -1

        return max_frogs

my_sol = Solution()

croakOfFrogs = "croakcroak"
print(my_sol.minNumberOfFrogs(croakOfFrogs)) #1

croakOfFrogs = "crcoakroak"
print(my_sol.minNumberOfFrogs(croakOfFrogs)) #2

croakOfFrogs = "croakcrook"
print(my_sol.minNumberOfFrogs(croakOfFrogs)) #-1

croakOfFrogs = "croakcroa"
print(my_sol.minNumberOfFrogs(croakOfFrogs)) #-1
