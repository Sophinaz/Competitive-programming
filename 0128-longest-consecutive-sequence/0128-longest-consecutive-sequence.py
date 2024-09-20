class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        result = 0
        left = 0
        for right in range(1, len(nums)):
            if nums[right] - nums[right-1] != 1:
                left = right
            else:
                result = max(result, right - left + 1)
        if result:
            return result
        return 1