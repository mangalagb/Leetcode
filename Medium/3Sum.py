#Given an array nums of n integers, are there elements a, b, c in nums
# such that a + b + c = 0? Find all unique triplets in the array which
# gives the sum of zero.

#The solution set must not contain duplicate triplets.


def findSum(nums):
    length_nums = len(nums)
    if length_nums == 0:
        return []

    numbers = sorted(nums)
    result = []
    unique_numbers = set()

    for k in range(0,length_nums -1):
        i = k+1
        j = len(nums) -1

        if numbers[i] == numbers[j] and len(result) != 0:
            continue

        while i < j:
            if numbers[k] + numbers[i] + numbers[j] == 0:
                string_num = str(numbers[k]) + str(numbers[i]) + str(numbers[j])

                if string_num not in unique_numbers:
                    result.append([numbers[k], numbers[i], numbers[j]])
                    unique_numbers.add(string_num)

                i += 1
                j -= 1
            elif numbers[k] + numbers[i] + numbers[j] < 0:
                i += 1
            elif numbers[k] + numbers[i] + numbers[j] > 0:
                j -= 1
    return result

nums = [3,0,-2,-1,1,2]
print(findSum(nums))