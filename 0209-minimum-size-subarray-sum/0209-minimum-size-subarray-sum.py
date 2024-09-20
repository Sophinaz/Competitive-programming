class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        result = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while left <= right and total >= target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        if result == float('inf'):
            return 0
        return result