
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf') 
        for i in nums:
            if i > first and i > second:
                return True
            if i == first or i == second:
                continue
            if i < first:
                first = i
            elif i < second:
                second = i
        return False

