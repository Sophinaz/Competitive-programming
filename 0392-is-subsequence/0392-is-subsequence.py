class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t or len(s) > len(t): return False
        
        def valid(r, c):
            return 0 <= r < len(s) and 0 <= c < len(t)
        dp = [[False for i in range(len(t))] for i in range(len(s))]
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    if valid(i-1, j-1):
                        dp[i][j] = dp[i-1][j-1]
                    else: 
                        dp[i][j] = True

                else:
                    if valid(i, j-1): dp[i][j] = dp[i][j-1]
                    else: dp[i][j] = False

        return dp[-1][-1]