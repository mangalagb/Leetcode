# Alice has a hand of cards, given as an array of integers.
#
# Now she wants to rearrange the cards into groups so that
# each group is size W, and consists of W consecutive cards.
#
# Return true if and only if she can.
#
# Note: This question is the same as 1296:
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

#If you store items you want to remove in a blacklist set, then
# each time you heapq.heappop check if that item is in the set.
# If it exists discard it and heappop again until you get something
# that's not blacklisted, or the heap is empty

import heapq

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        hand_len = len(hand)
        if hand_len % W != 0 or W > hand_len:
            return False

        heapq.heapify(hand)
        blacklist = []

        while len(hand) > 0:
            smallest = None
            while len(hand) > 0:
                smallest = heapq.heappop(hand)
                if smallest not in blacklist:
                    break
                else:
                    blacklist.remove(smallest)

            if len(hand) == 0:
                return True

            for i in range(1, W):
                next_num = smallest+i
                if next_num not in hand:
                    return False
                else:
                    blacklist.append(next_num)
        return True


my_sol = Solution()

hand = [2,3,1]
W = 3
print(my_sol.isNStraightHand(hand, W)) #True

hand = [2,1]
W = 2
print(my_sol.isNStraightHand(hand, W)) #True


hand = [1,2,3,6,2,3,4,7,8]
W = 3
print(my_sol.isNStraightHand(hand, W)) #True

hand = [1,2,3,4,5,5,5,5]
W = 4
print(my_sol.isNStraightHand(hand, W)) #False

hand = [1,2,3]
W = 1
print(my_sol.isNStraightHand(hand, W)) #True

hand = [8,10,12]
W = 3
print(my_sol.isNStraightHand(hand, W)) #False
