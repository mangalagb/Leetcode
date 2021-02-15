# Given the availability time slots arrays slots1 and slots2 of two
# people and a meeting duration duration, return the earliest time
# slot that works for both of them and is of duration duration.
#
# If there is no common time slot that satisfies the requirements,
# return an empty array.
#
# The format of a time slot is an array of two elements [start, end]
# representing an inclusive time range from start to end.
#
# It is guaranteed that no two availability slots of the same person
# intersect with each other. That is, for any two time slots [start1, end1]
# and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        i = 0
        j = 0

        slots1 = self.sort_time_slots(slots1)
        slots2 = self.sort_time_slots(slots2)

        while i < len(slots1) and j < len(slots2):
            element1 = slots1[i]
            start1 = element1[0]
            end1 = element1[1]

            element2 = slots2[j]
            start2 = element2[0]
            end2 = element2[1]

            #if start1 <= start2 <= end1 or start1 <= end2 <= end1:
            if start1 <= end2 or start2 <= end1:
                new_start = max(start1, start2)
                new_end = min(end1, end2)
                diff = new_end - new_start

                if diff >= duration:
                    ans = [new_start, new_start+duration]
                    return ans

            if end1 >= end2:
                j += 1
            else:
                i += 1

        return []

    def sort_time_slots(self, slots):
        slot_dict = {}

        for slot in slots:
            start = slot[0]

            if start not in slot_dict:
                slot_dict[start] = [slot]
            else:
                slot_dict[start].append(slot)

        result = []
        for key in sorted(slot_dict):
            slots = slot_dict[key]
            result.extend(slots)
        return result




my_sol = Solution()

slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 8
print(my_sol.minAvailableDuration(slots1, slots2, duration)) #[60, 68]

slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 12
print(my_sol.minAvailableDuration(slots1, slots2, duration)) #[]

slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 1
print(my_sol.minAvailableDuration(slots1, slots2, duration)) #[10, 11]

slots1 = [[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]]
slots2 = [[50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]]
duration = 456085
print(my_sol.minAvailableDuration(slots1, slots2, duration)) #[98730764,99186849]



