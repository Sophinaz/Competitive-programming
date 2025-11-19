class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = float('-inf')
        summ = 0

        for i in range(n):
            summ += nums[i]
            total = max(total, summ)
            if summ < 0:
                summ = 0

        return total