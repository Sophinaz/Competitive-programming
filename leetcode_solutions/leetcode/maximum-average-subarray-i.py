class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        total = 0
        for i in range(k):
            total += nums[i]
        average = total / k
        for i in range(k,len(nums)):
            total += nums[i]
            total -= nums[left]
            average = max(average,total/k)
            left += 1
        return average