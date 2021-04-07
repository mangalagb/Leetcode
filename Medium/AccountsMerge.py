#Given a list accounts, each element accounts[i] is a list of strings,
# where the first element accounts[i][0] is a name, and the rest of the
# elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong
# to the same person if there is some email that is common to both accounts.
# Note that even if two accounts have the same name, they may belong to
# different people as people could have the same name. A person can have
# any number of accounts initially, but all of their accounts definitely have the same name.
#
# After merging the accounts, return the accounts in the following
# format: the first element of each account is the name, and the
# rest of the elements are emails in sorted order. The accounts
# themselves can be returned in any order.
import collections


class Solution(object):
    def accountsMerge(self, accounts):
        email_to_name = {}
        graph = collections.defaultdict(set)
        for account in accounts:
            name = account[0]
            emails = account[1:]

            first = account[1]
            for email in emails:
                graph[first].add(email)
                graph[email].add(first)
                email_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                result = self.do_DFS(seen, email, graph, email_to_name)
                ans.append(result)
        return ans

    def do_DFS(self, seen, email, graph, email_to_name):
        seen.add(email)
        stack = [email]
        local_result = []
        while stack:
            node = stack.pop()
            local_result.append(node)
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)
        result = sorted(local_result)
        result.insert(0, email_to_name[email])
        return result



my_sol = Solution()

# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
#             ["John", "johnnybravo@mail.com"],
#             ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
#             ["Mary", "mary@mail.com"]]
# print(my_sol.accountsMerge(accounts))
# # #[["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
# # # ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
#
# accounts = [["David","David0@m.co","David1@m.co"],
#             ["David","David3@m.co","David4@m.co"],
#             ["David","David4@m.co","David5@m.co"],
#             ["David","David2@m.co","David3@m.co"],
#             ["David","David1@m.co","David2@m.co"]]
# print(my_sol.accountsMerge(accounts))
# # #[["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]

accounts = [["Hanzo","Hanzo2@m.co","Hanzo3@m.co"],
            ["Hanzo","Hanzo4@m.co","Hanzo5@m.co"],
            ["Hanzo","Hanzo0@m.co","Hanzo1@m.co"],
            ["Hanzo","Hanzo3@m.co","Hanzo4@m.co"],
            ["Hanzo","Hanzo7@m.co","Hanzo8@m.co"],
            ["Hanzo","Hanzo1@m.co","Hanzo2@m.co"],
            ["Hanzo","Hanzo6@m.co","Hanzo7@m.co"],
            ["Hanzo","Hanzo5@m.co","Hanzo6@m.co"]]
print(my_sol.accountsMerge(accounts))

# accounts = [["Gabe","Gabe5@m.co","Gabe45@m.co","Gabe46@m.co","Gabe47@m.co","Gabe48@m.co","Gabe49@m.co","Gabe50@m.co","Gabe51@m.co","Gabe52@m.co"],["Gabe","Gabe3@m.co","Gabe27@m.co","Gabe28@m.co","Gabe29@m.co","Gabe30@m.co","Gabe31@m.co","Gabe32@m.co","Gabe33@m.co","Gabe34@m.co"],["Gabe","Gabe6@m.co","Gabe54@m.co","Gabe55@m.co","Gabe56@m.co","Gabe57@m.co","Gabe58@m.co","Gabe59@m.co","Gabe60@m.co","Gabe61@m.co"],["Gabe","Gabe0@m.co","Gabe0@m.co","Gabe1@m.co","Gabe2@m.co","Gabe3@m.co","Gabe4@m.co","Gabe5@m.co","Gabe6@m.co","Gabe7@m.co"],["Gabe","Gabe1@m.co","Gabe9@m.co","Gabe10@m.co","Gabe11@m.co","Gabe12@m.co","Gabe13@m.co","Gabe14@m.co","Gabe15@m.co","Gabe16@m.co"],["Gabe","Gabe2@m.co","Gabe18@m.co","Gabe19@m.co","Gabe20@m.co","Gabe21@m.co","Gabe22@m.co","Gabe23@m.co","Gabe24@m.co","Gabe25@m.co"],["Gabe","Gabe4@m.co","Gabe36@m.co","Gabe37@m.co","Gabe38@m.co","Gabe39@m.co","Gabe40@m.co","Gabe41@m.co","Gabe42@m.co","Gabe43@m.co"],["Gabe","Gabe0@m.co","Gabe0@m.co","Gabe1@m.co","Gabe2@m.co","Gabe3@m.co","Gabe4@m.co","Gabe5@m.co","Gabe6@m.co","Gabe7@m.co"]]
# print(my_sol.accountsMerge(accounts))
#[["Gabe","Gabe0@m.co","Gabe10@m.co","Gabe11@m.co","Gabe12@m.co","Gabe13@m.co","Gabe14@m.co","Gabe15@m.co","Gabe16@m.co","Gabe18@m.co","Gabe19@m.co","Gabe1@m.co","Gabe20@m.co","Gabe21@m.co","Gabe22@m.co","Gabe23@m.co","Gabe24@m.co","Gabe25@m.co","Gabe27@m.co","Gabe28@m.co","Gabe29@m.co","Gabe2@m.co","Gabe30@m.co","Gabe31@m.co","Gabe32@m.co","Gabe33@m.co","Gabe34@m.co","Gabe36@m.co","Gabe37@m.co","Gabe38@m.co","Gabe39@m.co","Gabe3@m.co","Gabe40@m.co","Gabe41@m.co","Gabe42@m.co","Gabe43@m.co","Gabe45@m.co","Gabe46@m.co","Gabe47@m.co","Gabe48@m.co","Gabe49@m.co","Gabe4@m.co","Gabe50@m.co","Gabe51@m.co","Gabe52@m.co","Gabe54@m.co","Gabe55@m.co","Gabe56@m.co","Gabe57@m.co","Gabe58@m.co","Gabe59@m.co","Gabe5@m.co","Gabe60@m.co","Gabe61@m.co","Gabe6@m.co","Gabe7@m.co","Gabe9@m.co"]]
