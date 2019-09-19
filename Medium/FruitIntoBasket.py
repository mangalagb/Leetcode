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

class Solution(object):

    def totalFruit(self, tree):
        if not tree:
            return 0
        #print(tree)

        first_fruit = None
        second_fruit = None

        first_fruit_count = 0
        second_fruit_count = 0

        index_where_fruit_changed = -1
        total_fruit = 0
        previous_fruit = None

        for i in range(0, len(tree)):
            fruit = tree[i]
            if first_fruit is None:
                first_fruit = fruit
                first_fruit_count += 1

                index_where_fruit_changed = i
                previous_fruit = fruit

                local_total_fruit = first_fruit_count + second_fruit_count
                if local_total_fruit > total_fruit:
                    total_fruit = local_total_fruit
                continue

            elif fruit != first_fruit and second_fruit is None:
                second_fruit = fruit
                second_fruit_count += 1

                if fruit != previous_fruit:
                    previous_fruit = fruit
                    index_where_fruit_changed = i

                local_total_fruit = first_fruit_count + second_fruit_count
                if local_total_fruit > total_fruit:
                    total_fruit = local_total_fruit
                continue

            if fruit == first_fruit:
                first_fruit_count += 1
                if fruit != previous_fruit:
                    previous_fruit = fruit
                    index_where_fruit_changed = i

            elif fruit == second_fruit:
                second_fruit_count += 1
                if fruit != previous_fruit:
                    previous_fruit = fruit
                    index_where_fruit_changed = i
            else:
                first_fruit = previous_fruit
                first_fruit_count = i - index_where_fruit_changed

                previous_fruit = fruit
                index_where_fruit_changed = i

                second_fruit = fruit
                second_fruit_count = 1

            local_total_fruit = first_fruit_count + second_fruit_count
            if local_total_fruit > total_fruit:
                total_fruit = local_total_fruit

        return total_fruit


my_sol = Solution()

tree = [1,2,1]
print(my_sol.totalFruit(tree))

tree = [0,1,2,2]
print(my_sol.totalFruit(tree))

tree = [1,2,3,2,2]
print(my_sol.totalFruit(tree))

tree = [3,3,3,1,2,1,1,2,3,3,4]
print(my_sol.totalFruit(tree))

tree = [0,0,0,0,0,0,0]
print(my_sol.totalFruit(tree))