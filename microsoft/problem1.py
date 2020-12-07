# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(Y, A, B, W):
    # write your code in Python 3.6
    is_leap_year = False
    if Y % 4 == 0:
        is_leap_year = True

    start_month = get_months(A)
    end_month = get_months(B)

    total_days = 0
    for i in range(start_month, end_month+1):
        total_days += get_days(i, is_leap_year)

    weeks = total_days // 8
    return weeks


def get_months(month):
    if month == "January":
        return 1
    elif month == "February":
        return 2
    elif month == "March":
        return 3
    elif month == "April":
        return 4
    elif month == "May":
        return 5
    elif month == "June":
        return 6
    elif month == "July":
        return 7
    elif month == "August":
        return 8
    elif month == "September":
        return 9
    elif month == "October":
        return 10
    elif month == "November":
        return 11
    elif month == "December":
        return 12


def get_days(month, is_leap_year):
    #31, 28 (or 29 in a leap year), 31,  30, 31, 30, 31, 31, 30, 31, 30, 31
    if month == 1:
        return 31
    elif month == 2:
        if is_leap_year:
            return 29
        else:
            return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31






Y = 2014
A = "April"
B = "May"
W = "Wednesday" #7

print(solution(Y, A, B, W))