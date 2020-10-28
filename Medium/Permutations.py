# Given a collection of distinct integers, return all possible permutations.

def find_combinations(nums):
    length = len(nums)

    if length == 1:
        return [[nums[0]]]
    else:
        constant = nums[0]
        result = find_combinations(nums[1:len(nums)])

        temp_result = []
        for permutation in result:
            for i in range(0,len(permutation)):
                temp = permutation[0:i] + [constant] + permutation[i:len(permutation)]
                temp_result.append(temp)
            temp_result.append(permutation + [constant])
        return temp_result


def permute(nums):
    length = len(nums)

    if length == 0:
        return []
    elif length == 1:
        return [[nums[0]]]

    return find_combinations(nums)


# nums = [1,2]
# print(permute(nums))

nums = [1,2,3]
print(permute(nums))
