#Given a characters array tasks, representing the tasks a CPU
# needs to do, where each letter represents a different task.
# Tasks could be done in any order. Each task is done in one unit of time.
# For each unit of time, the CPU could complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the
# cooldown period between two same tasks (the same letter in the array),
# that is that there must be at least n units of time between any two same tasks.
#
# Return the least number of units of times that the CPU will
# take to finish all the given tasks.

import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_dict = {}
        for task in tasks:
            if task not in task_dict:
                task_dict[task] = 1
            else:
                task_dict[task] += 1

        # Push all tasks in heap
        my_heap = []
        for key, value in task_dict.items():
            values = [-value, key]
            heapq.heappush(my_heap, values)

        total_count = 0
        while len(my_heap) > 0:
            interval_count = n + 1
            temp_items = []

            while len(my_heap) > 0 and interval_count > 0:
                popped_item = heapq.heappop(my_heap)

                #Update its value
                popped_item[0] += 1
                temp_items.append(popped_item)

                #One slot has been occupied
                total_count += 1

                #Decrement interval
                interval_count -= 1

            #Put back the items in the heap
            for item in temp_items:
                if item[0] < 0:
                    heapq.heappush(my_heap, item)

            if len(my_heap) == 0:
                break

            #Even after filling tasks, there is spot left in interval.
            #So it shoud be idle
            if interval_count > 0:
                total_count += interval_count

        return total_count


my_sol = Solution()

tasks = ["A","A","A","B","B","B","C","C","C", "D", "D", "E"]
n = 2
print(my_sol.leastInterval(tasks, n)) #12


tasks = ["A","A","A","B","B","B"]
n = 2
print(my_sol.leastInterval(tasks, n)) #8

tasks = ["A","A","A","B","B","B"]
n = 0
print(my_sol.leastInterval(tasks, n)) #6

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(my_sol.leastInterval(tasks, n)) #16

