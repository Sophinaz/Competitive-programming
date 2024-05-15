class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(n, sofar):
            if sofar == amount: return 1
            if sofar > amount or n >= len(coins): return 0
            
            count = 0
            for i in range(n, len(coins)):
                count += dp(i, sofar + coins[i])

            return count
        return dp(0, 0)