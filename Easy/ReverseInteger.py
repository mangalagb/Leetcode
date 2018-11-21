class Solution(object):
    def reverse(self, x):

        if x == 0:
            return 0

        negative_number = False
        num = x
        if x < 0:
            negative_number = True
            num = -1 * x

        largest_number = str(pow(2, 31) - 1)
        smallest_number = str(pow(-2, 31) * -1)

        print(largest_number, smallest_number)

        # Remove trailing zeroes
        num_str = str(num)
        for i in range(len(num_str)-1, -1, -1):
            if num_str[i] != '0':
                break
            else:
                num_str = num_str[:len(num_str)-1]

        num = int(num_str)

        to_check = False
        if len(num_str) > len(largest_number):
            return 0
        elif len(num_str) == len(largest_number):
            to_check = True

        reversed_num = 0
        number_counter = 0
        while num != 0:
            digit = num % 10
            num = num // 10

            reversed_num = (reversed_num*10) + digit
            if to_check:

                if not negative_number:
                    if digit > int(largest_number[number_counter]):
                        return 0
                    elif digit == int(largest_number[number_counter]):
                        number_counter += 1
                    else:
                        to_check = False
                else:
                    if digit > int(smallest_number[number_counter]):
                        return 0
                    elif digit == int(smallest_number[number_counter]):
                        number_counter += 1
                    else:
                        to_check = False

        if negative_number:
            return -1 * reversed_num
        else:
            return reversed_num



my_sol = Solution()

print(my_sol.reverse(-2147483412))
#-2143847412

#print(my_sol.reverse(123))