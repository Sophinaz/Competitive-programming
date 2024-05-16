class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, state):
            if i >= len(prices): return 0

            if state == 0 or state == 2:
                if state == 0:
                    return max(dp(i+1, 1) - prices[i], dp(i+1, 0)) 
                if state == 2:
                    return max(dp(i+1, 3) - prices[i], dp(i+1, 2)) 
            else:
                if state == 1:
                    return max(dp(i+1, 2) + prices[i], dp(i+1, 1)) 
                else: return prices[i]
        return dp(0,0)