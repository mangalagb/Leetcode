class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans  = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                string = str("FizzBuzz")
                ans.append(string)
            elif i % 3 == 0:
                string = str("Fizz")
                ans.append(string)
            elif i % 5 == 0:
                string = str("Buzz")
                ans.append(string)
            else:
                ans.append(str(i))
        return ans




my_sol = Solution()
print(my_sol.fizzBuzz(15))
