class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        result = deque()
        for i in deck:
            if not result: 
                result.appendleft(i)
                continue
            
            result.appendleft(result.pop())
            result.appendleft(i)

        return result