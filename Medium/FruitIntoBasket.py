# In a row of trees, the i-th tree produces fruit with type tree[i].
#
# You start at any tree of your choice, then repeatedly perform the following
#  steps:
#
#     Add one piece of fruit from this tree to your baskets.  If you cannot,
#  stop.
#     Move to the next tree to the right of the current tree.  If there is
# no tree to the right, stop.
#
# Note that you do not have any choice after the initial choice of starting
#  tree: you must perform step 1, then step 2, then back to step 1, then step
#  2, and so on until you stop.
#
# You have two baskets, and each basket can carry any quantity of fruit, but
#  you want each basket to only carry one type of fruit each.
#
# What is the total amount of fruit you can collect with this procedure?

# Longest contigous subarry of 2 numbers

#SOLUTION
# https://www.youtube.com/watch?v=s_zu2dOkq80

class Solution(object):

    def totalFruit(self, tree):
        if not tree:
            return 0

        last_fruit = -1
        second_last_fruit = -1
        last_fruit_count = 0

        final_max = 0
        current_max = 0

        for current_fruit in tree:
            if current_fruit == last_fruit or current_fruit == second_last_fruit:
                current_max += 1
            else:
                current_max = last_fruit_count + 1

            if current_fruit == last_fruit:
                last_fruit_count += 1
            else:
                last_fruit_count = 1

            if current_fruit != last_fruit:
                second_last_fruit = last_fruit
                last_fruit = current_fruit

            final_max = max(final_max, current_max)
        return final_max


my_sol = Solution()

tree = [1,2,1]
print(my_sol.totalFruit(tree)) #3

tree = [0,1,2,2]
print(my_sol.totalFruit(tree)) #3

tree = [1,2,3,2,2]
print(my_sol.totalFruit(tree)) #4
#
# tree = [3,3,3,1,2,1,1,2,3,3,4]
# print(my_sol.totalFruit(tree))
#
# tree = [0,0,0,0,0,0,0]
# print(my_sol.totalFruit(tree))