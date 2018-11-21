class Solution(object):
    def findItinerary(self, tickets):
        airports, visited = self.construct_graph(tickets)

        path = []
        path.append("JFK")
        airports_copy = airports.copy()

        from_airport = "JFK"
        counter = 0

        while len(airports) != 0:
            values = airports[from_airport]

            if values:
                temp = values[counter]
                visited[from_airport] = True
                self.visit(from_airport, values[counter], airports, path,
                           visited)
                from_airport = temp
            else:
                if self.check_visited(visited):
                    break
                else:
                    #self.reset_visited(visited)
                    airports, visited = self.construct_graph(tickets)
                    counter += 1
                    path.clear()
                    path.append("JFK")
                    from_airport = "JFK"

        return path

    def reset_visited(self, visited):
        for key in visited.keys():
            visited[key] = False

    def check_visited(self, visited):
        for key in visited.keys():
            if not visited[key]:
                return False
        return True

    def visit(self, from_airport, to_airport, airports, path, visited):
        path.append(to_airport)
        visited[to_airport] = True

        values = airports[from_airport]

        if values:
            values.remove(to_airport)
        else:
            airports.pop(from_airport, None)

        #return airports, path, visited

    def construct_graph(self, tickets):
        airports = {}

        for ticket in tickets:
            from_airport = ticket[0]
            to_airport = ticket[1]

            if from_airport not in airports:
                airports[from_airport] = [to_airport]
            else:
                values = airports[from_airport]
                values.append(to_airport)
                airports[from_airport] = values

            if to_airport not in airports:
                airports[to_airport] = []

        visited = {}
        for airport in airports:
            values = airports[airport]
            airports[airport] = sorted(values)

            visited[airport] = False
        return airports, visited



my_sol = Solution()

# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# print(tickets)
# print(my_sol.findItinerary(tickets))

# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# print(my_sol.findItinerary(tickets))

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(tickets)
print(my_sol.findItinerary(tickets))

