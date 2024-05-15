class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        memo = {}
        def dp(n):
            if n not in memo:
                if n < 4:
                    return n
                ans = float('-inf')
                for i in range(2, n//2+1):
                    ans = max(ans, dp(i) * dp(n-i)) 
                memo[n] = ans

            return memo[n]
        return dp(n)
