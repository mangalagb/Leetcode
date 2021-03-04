#You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a
# type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels_set = set()
        for character in jewels:
            jewels_set.add(character)

        num_of_jewels = 0
        for stone in stones:
            if stone in jewels_set:
                num_of_jewels += 1
        return num_of_jewels



my_sol = Solution()

jewels = "aA"
stones = "aAAbbbb"
print(my_sol.numJewelsInStones(jewels, stones)) #3

jewels = "z"
stones = "ZZ"
print(my_sol.numJewelsInStones(jewels, stones)) #0

