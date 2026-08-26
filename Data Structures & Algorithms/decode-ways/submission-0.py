class Solution:
    def numDecodings(self, s: str) -> int:
        # so we are told that strings can be enocded by numbers from 1 - 26
    # we are given the task to decode the string by find how many different ways can the number be decoded as ex s = 12 this can be decoded as ab or L as you can decode each number or decode the entire number they are still correct.
  # the dp relation could be to find the different combination of decoded letters s could represent. 
  # at each index we can either decode the current digit or combine with the one next to it 



        dp = {len(s) : 1}

        for i in range(len(s) -1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                dp[i] += dp[i+2]
        
        return dp[0]





