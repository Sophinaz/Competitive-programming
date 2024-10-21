class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(l, r, turn):
            if l > r: return 0
            if turn:
                return max(dp(l+1, r, False) + piles[l], dp(l, r-1, False) + piles[r])
            else:
                return min(dp(l+1, r, True) - piles[l], dp(l, r-1, True) - piles[r])

        result = dp(0, len(piles)-1, True)
        if result: return True
        return False