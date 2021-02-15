#There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
#
# You have to form a team of 3 soldiers amongst them under the following rules:
#
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if:  (rating[i] < rating[j] < rating[k]) or
# (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions.
# (soldiers can be part of multiple teams).

class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        rating_length = len(rating)
        forward_array = {}
        backward_array = {}

        for i in range(0, rating_length):
            forward_array[rating[i]] = []
            backward_array[rating[i]] = []

        for i in range(0, rating_length):
            for j in range(i+1, rating_length):
                if rating[i] < rating[j]:
                    forward_array[rating[i]].append(rating[j])

        for i in range(0, rating_length):
            for j in range(i+1, rating_length):
                if rating[i] > rating[j]:
                    backward_array[rating[i]].append(rating[j])

        count = 0
        for key, values in forward_array.items():
            for value in values:
                third_results = forward_array[value]
                for item in third_results:
                    if item > value:
                        count += 1

        for key, values in backward_array.items():
            for value in values:
                third_results = backward_array[value]
                for item in third_results:
                    if item < value:
                        count += 1
        return count

my_sol = Solution()

rating = [2,5,3,4,1]
print(my_sol.numTeams(rating)) #3

rating = [2,1,3]
print(my_sol.numTeams(rating)) #0

rating = [1,2,3,4]
print(my_sol.numTeams(rating)) #4
