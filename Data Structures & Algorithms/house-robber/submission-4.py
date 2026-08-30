class Solution:
    def rob(self, nums: List[int]) -> int:
        # i need to figure the max zmount of money we can make from robbing houses we know that we cannot rob two adjacent houses so we need to find the combination of houses that when robbed given the highest return.
        # ;;

        # nums = [2,9,8,3,6]

        #             

        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])

        for i in range(2,len(nums)):
            dp[i] = max(nums[i] + dp[i-2],dp[i-1])
        
        return dp[-1]

        
