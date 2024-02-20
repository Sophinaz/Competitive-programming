class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        result = 0
        for i in costs:
            if coins < i:
                break
            result += 1
            coins -= i
        return result