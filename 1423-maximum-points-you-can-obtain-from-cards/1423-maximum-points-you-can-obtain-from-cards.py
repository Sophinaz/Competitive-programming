class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k 
        total = sum(cardPoints[r:])
        result = total
        while r < len(cardPoints) and l < len(cardPoints):
            total -= cardPoints[r]
            total += cardPoints[l]
            result = max(result, total)
            l += 1
            r += 1
        return result
