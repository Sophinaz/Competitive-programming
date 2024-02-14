class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles,reverse=True)
        l=1
        r=len(piles)-1
        result = 0
        while l < r:
            result += piles[l]
            l+=2
            r-=1
        return result
        