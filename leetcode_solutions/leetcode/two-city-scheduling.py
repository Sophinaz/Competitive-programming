class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        nums = sorted(costs, key = lambda x: x[0] - x[1])
        total = 0
        for i in range(len(nums)//2):
            total += nums[i][0]
        for i in range(len(nums)//2,len(nums)):
            total += nums[i][1]
        return total