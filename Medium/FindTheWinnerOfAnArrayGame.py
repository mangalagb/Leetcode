# #Given an integer array arr of distinct integers and an integer k.
#
# A game will be played between the first two elements of the array
# (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0]
# with arr[1], the larger integer wins and remains at position 0 and the
# smaller integer moves to the end of the array. The game ends when an integer
# wins k consecutive rounds.
#
# Return the integer which will win the game.
#
# It is guaranteed that there will be a winner of the game.

class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(arr):
            return max(arr)

        num_of_wins_of_first = 0
        while True:
            first = arr[0]
            second = arr[1]

            if first > second:
                #Keep count of wins
                num_of_wins_of_first += 1
                if num_of_wins_of_first == k:
                    return first

                #Move second to end of array
                arr.remove(second)
                arr.append(second)
            else:
                #Move first to end of array
                arr.remove(first)
                arr.append(first)

                #Set num of wins
                num_of_wins_of_first = 1
                if num_of_wins_of_first == k:
                    return second




my_sol = Solution()

arr = [2,1,3,5,4,6,7]
k = 2
print(my_sol.getWinner(arr, k)) #5

arr = [3,2,1]
k = 10
print(my_sol.getWinner(arr, k)) #3

arr = [1,9,8,2,3,7,6,4,5]
k = 7
print(my_sol.getWinner(arr, k)) #9

arr = [1,11,22,33,44,55,66,77,88,99]
k = 1000000000
print(my_sol.getWinner(arr, k)) #99

arr = [1,25,35,42,68,70]
k = 1
print(my_sol.getWinner(arr, k)) #25

