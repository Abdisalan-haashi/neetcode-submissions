class Solution:
    def climbStairs(self, n: int) -> int:
        # the question is asking us to find the different amount of we can climb n climbStairs
        # this problem can be solved using dp as dp[i] represents
        # the number of ways we can climb the stair [i] times
        # the relation between is that the previous answers will always add up to the current answers


        if n <= 2:
            return n
        

        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[-1]


