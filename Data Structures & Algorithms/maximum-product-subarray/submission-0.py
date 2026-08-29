class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        res = nums[0]
        CurrMax,CurrMin = 1,1

        for n in nums:
            if n == 0:
                CurrMax,CurrMin = 1,1

            tmp = n*CurrMax
            CurrMax = max(n*CurrMax, n*CurrMin, n)
            CurrMin = min(tmp, n*CurrMin,n)
            res = max(res,CurrMax)
    
        return res




      

      








