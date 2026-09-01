class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # so the problem is asking us to find whether we can for the words in the dictionary from our string s. it wants to find out whether the words can be segmented into the worddict. the brute force approach would be to compare every single character in string s and check if its in the word dict'



        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if(i + len(w) <= len(s) and s[i: i + len(w)] == w):
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]
        