class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # so we are given an array of coins and we need to find the minimum amount of coins when added together equal the total. we also know that each coin can be reused multiple times and that there can be cases where its impossible and cases where you dont return any coin.


        dp = [amount + 1] * (amount + 1)
        dp[0] = 0


        for a in range(1, amount + 1): # build each amount to get to the final
            for c in coins:# check the possiblity of each coin to make that amount
                if a - c >=0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
                
        
        return dp[amount] if dp[amount] != amount + 1 else -1

