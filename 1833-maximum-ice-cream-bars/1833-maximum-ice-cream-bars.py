class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        result = 0
        count  =0
        for i in costs:
            result += i
            if result <= coins:
                count += 1
            else: break
        return count
        