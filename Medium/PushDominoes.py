#There are N dominoes in a line, and we place each domino vertically upright.
# In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
# After each second, each domino that is falling to the left pushes the adjacent domino on the left.

# Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
#
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
#
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling
# or already fallen domino.
#
# Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left;
# S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.
#
# Return a string representing the final state.

class Solution(object):
    def pushDominoes(self, dominoes):
        characters = [char for char in dominoes]

        length_of_characters = len(characters)
        if length_of_characters < 2:
            return dominoes

        indexes = []
        for i in range(0, len(characters)):
            if characters[i] != ".":
                indexes.append(i)

        if len(indexes) == 0:
            return dominoes

        indexes.append(-1)
        count = 0
        begin = 0
        end = indexes[count]

        while end < length_of_characters and begin < length_of_characters:
            end = indexes[count]
            begin_char = characters[begin]
            if end == -1:
                if begin_char == "R":
                    for i in range(begin, length_of_characters):
                        characters[i] = begin_char
                break

            end_char = characters[end]

            if begin == 0 and begin_char == "." and end_char == "L":
                for i in range(begin, end):
                    characters[i] = end_char
                begin = indexes[count]
                count += 1
                continue

            if begin_char == "R" and end_char == "L":
                while begin != end and begin+1 != end and begin+1 != end-1 and begin+1 < length_of_characters:
                    characters[begin + 1] = characters[begin]
                    characters[end - 1] = characters[end]
                    begin += 1
                    end -= 1

            elif begin_char == "L" and end_char == "L":
                for i in range(begin + 1, end):
                    if i < length_of_characters:
                        characters[i] = end_char
                    else:
                        break

            elif begin_char == "R" and end_char == "R":
                for i in range(begin + 1, end):
                    if i < length_of_characters:
                        characters[i] = begin_char
                    else:
                        break

            begin = indexes[count]
            count += 1

        result = ''.join(characters)
        return result

my_sol = Solution()

input = ".L.R...LR..L.."
print(my_sol.pushDominoes(input))   # LL.RR.LLRRLL..

input = "RR.L"
print(my_sol.pushDominoes(input))   # RR.L

input = ".L.R."
print(my_sol.pushDominoes(input))   # "LL.RR"

input = "RL"
print(my_sol.pushDominoes(input))   # "RL"

