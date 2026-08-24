class Solution:
    def countSubstrings(self, s: str) -> int:
        # so the questio is asking me to return the amount of palindromes within a string 
        # whats considered a palindrome is characters by itself is automatically one along with characters that read the same front and back
        
        n = len(s)
        res = 0

        dp = [[False] * n for _ in range(n)]

        for i in range(n -1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j] and ((j - i <= 2) or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1

        return res

    