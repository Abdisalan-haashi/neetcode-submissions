class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we need to find the longest palindrome within a string
        # a palindrome is when a string is read the same forward and backwards so the characters and positions are the same
        # we first need to find the reccurence relation so that could be starting from the 

        res = ""
        n = len(s)

        dp = [[False] * n for _ in range(n)] 

        for i in range(n -1, -1, -1):
            for j in range(i,n):
                if s[j] == s[i] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

                    if (j - i + 1) > len(res):
                        res = s[i:j + 1]

        
        return res