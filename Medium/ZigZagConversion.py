# The string "PAYPALISHIRING" is written in a zigzag pattern on a given
#  number of rows like this: (you may want to display this pattern in a
# fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows

class Solution(object):
    def convert(self, s, numRows):
        if not s:
            return ""

        matrix = []
        use_only_rows = False
        to_fill_zig_zag = True
        for i in range(0, numRows):
            matrix.append([])

        possible_numbers = []
        if numRows == 1:
            possible_numbers = [1]
            to_fill_zig_zag = False
        elif numRows == 2:
            use_only_rows = True
        else:
            possible_numbers = [i for i in range(numRows-2, 0, -1)]

        to_fill_counter = None
        if possible_numbers:
            to_fill_counter = possible_numbers[0]
        fill_row = True
        fil_col = 0

        for char in s:
            if fill_row and fil_col < numRows:
                values = matrix[fil_col]
                values.append(char)
                fil_col += 1
            elif use_only_rows:
                fil_col = 0
                values = matrix[fil_col]
                values.append(char)
                fil_col += 1
            else:
                fill_row = False
                fil_col = 0


            if not to_fill_zig_zag:
                fil_col -= 1

            if not fill_row and to_fill_counter is not None and to_fill_zig_zag:
                values = matrix[to_fill_counter]
                values.append(char)

                to_fill_counter -= 1
                if to_fill_counter not in possible_numbers:
                    to_fill_counter = possible_numbers[0]
                    fill_row = True

        result = ""
        for i in range(0, numRows):
            row = matrix[i]
            for char in row:
                result = result + char
        return result


my_sol = Solution()


s = "PAYPALISHIRING"
numRows = 3
print(my_sol.convert(s, numRows))

s = "PAYPALISHIRING"
numRows = 4
print(my_sol.convert(s, numRows))

s = "A"
numRows = 1
print(my_sol.convert(s, numRows))

s = "AB"
numRows = 1
print(my_sol.convert(s, numRows))

s = "A"
numRows = 2
print(my_sol.convert(s, numRows))

s = "ABC"
numRows = 2
print(my_sol.convert(s, numRows))

s = "ABCD"
numRows = 2
print(my_sol.convert(s, numRows))


