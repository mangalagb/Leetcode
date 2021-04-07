#Given a list of airline tickets represented by pairs of departure
# and arrival airports [from, to], reconstruct the itinerary in order.
# All of the tickets belong to a man who departs from JFK. Thus, the
# itinerary must begin with JFK.

# Note:
#
# If there are multiple valid itineraries, you should return the
# itinerary that has the smallest lexical order when read as a
# single string. For example, the itinerary ["JFK", "LGA"] has
# a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj_list = self.make_graph(tickets)
        answer = self.do_DFS("JFK", adj_list)
        return answer

    def do_DFS(self, node, adj_list):
        stack = [node]
        result = []

        while len(stack) > 0:
            airport = stack[-1]

            neighbour = self.find_unvisited_neighbours(adj_list[airport])
            if neighbour:
                stack.append(neighbour)
            else:
                result.insert(0, airport)
                stack.pop(-1)
        return result


    def find_unvisited_neighbours(self, neighbours):
        if len(neighbours) > 0:
            for i in range(0, len(neighbours)):
                neighbour = neighbours[i]
                if neighbour != -1:
                    neighbours[i] = -1
                    return neighbour
            return None
        else:
            return None

    def make_graph(self, tickets):
        adj_list = {}

        for ticket in tickets:
            city1 = ticket[0]
            city2 = ticket[1]

            if city1 not in adj_list:
                adj_list[city1] = [city2]
            else:
                adj_list[city1].append(city2)

            if city2 not in adj_list:
                adj_list[city2] = []

        for key, values in adj_list.items():
            if len(values) > 1:
                result = self.sort_lexically(values)
                adj_list[key] = result
        return adj_list

    def sort_lexically(self, values):
        result = []
        smallest = None

        while len(values) > 0:
            for value in values:
                if not smallest:
                    smallest = value

                else:
                    is_sorted = self.is_sorted(smallest, value)
                    if not is_sorted:
                        smallest = value
            result.append(smallest)
            values.remove(smallest)
            smallest = None
        return result

    def is_sorted(self, word1, word2):
        wor1_len = len(word1)
        word2_len = len(word2)

        diff = wor1_len - word2_len
        if diff > 0:
            for i in range(0, diff):
                word2 = word2 + "."
        elif diff < 0:
            for i in range(0, diff):
                word1 = word1 + "."

        i = 0
        while i < len(word1):
            char1 = word1[i]
            char2 = word2[i]

            index1 = ord(char1)
            index2 = ord(char2)

            if char1 == ".":
                index1 = -1
            if char2 == ".":
                index2 = -1

            if index1 < index2:
                return True
            elif index1 > index2:
                return False
            i += 1
        return True


my_sol = Solution()

airports = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(my_sol.findItinerary(airports)) #["JFK", "MUC", "LHR", "SFO", "SJC"]

airports = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(my_sol.findItinerary(airports)) #["JFK","ATL","JFK","SFO","ATL","SFO"]

