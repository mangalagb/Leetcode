class Solution:
    def find_time(self, time):
        digits = [int(digit) for digit in time if digit.isdigit()]
        uniques = sorted(set(digits))
        pos = [uniques.index(digit) for digit in digits]

        for i in range(3, -1, -1):
            pos[i] += 1
            if pos[i] < len(uniques):
                digits[i] = uniques[pos[i]]
                if digits[2] < 6 and digits[0] * 10 + digits[1] < 24:
                    return "{}{}:{}{}".format(*digits)
            digits[i] = uniques[0]

        return "no solution"

    def nextClosestTime(self, time):

        times = time.split(":")
        hours = int(times[0])
        minutes = int(times[1])

        smallest_num = minutes % 10
        if minutes // 10 < smallest_num:
            smallest_num = minutes//10
        if hours % 10 < smallest_num:
            smallest_num = hours % 10
        if hours // 10 < smallest_num:
            smallest_num = hours//10

        numbers = set()
        numbers.add(minutes % 10)
        if minutes // 10 not in numbers:
            numbers.add(minutes // 10)
        if hours % 10 not in numbers:
            numbers.add(hours % 10)
        if hours // 10 not in numbers:
            numbers.add(hours // 10)


        print(hours, minutes, numbers)
        incremented = False
        string_minutes = times[1]
        string_hours = times[0]

        minutes +=1
        while minutes < 60:
            digit1 = minutes % 10
            digit2 = minutes // 10

            if digit1 in numbers and digit2 in numbers:
                incremented = True
                string_minutes = str(digit2) + str(digit1)
                break
            minutes += 1

        if not incremented:
            minutes = smallest_num * 10 + smallest_num
            if minutes == 0:
                string_minutes = "00"
            else:
                string_minutes = str(minutes)

            hours += 1
            while hours < 24:
                digit1 = hours % 10
                digit2 = hours // 10

                if digit1 in numbers and digit2 in numbers:
                    incremented = True
                    string_hours = str(digit2) + str(digit1)
                    break
                hours += 1

        if not incremented:
            hours = smallest_num * 10 + smallest_num
            if hours == 0:
                string_hours = "00"
            else:
                string_hours = str(hours)

        result = string_hours + ":" + string_minutes
        return result





my_sol = Solution()
# time = "19:34"
# print(my_sol.nextClosestTime(time))
#
# time = "23:59"
# print(my_sol.nextClosestTime(time))
#
# time = "24:00"
# print(my_sol.nextClosestTime(time))
#
# time = "19:00"
# print(my_sol.nextClosestTime(time))

# time = "20:48"
# print(my_sol.nextClosestTime(time))

time = "20:56"
print(my_sol.find_time(time))