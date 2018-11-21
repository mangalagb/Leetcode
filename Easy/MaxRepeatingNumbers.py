#  Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size

#Solution = O(N) + O(N) = O(N)


def find_count(nums, k):
    count_dict = {}

    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    #create a bucket of size n
    bucket_list = []
    bucket_list.append(None)
    for i in range(1, len(nums)+1):
        empty_list = []
        bucket_list.append(empty_list)
    #print(bucket_list)

    #Fill value in bucket according to frequency
    for element, frequency in count_dict.items():
        bucket_list[frequency].insert(0, element)
    #print(bucket_list)

    #Find top k elements
    count = 0
    result = []
    for i in range(len(bucket_list)-1, 0, -1):
        result_list = bucket_list[i]
        if len(result_list) != 0:
            for element in result_list:
                result.append(element)
                count += 1
            if count == k:
                break
    print(result)
    return result


nums = [1,1,1,2,2,2,3]
k = 2
find_count(nums, k)



