class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashed = {}
        result = len(cards) +2
        for i in range(len(cards)):
            if cards[i] not in hashed:
                hashed[cards[i]] = i
            else:
                result = min(result, i+1-(hashed[cards[i]]))
                hashed[cards[i]] = i
        if result == len(cards)+2: return -1
        else:
            return result

        