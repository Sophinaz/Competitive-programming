class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        first = nums[-4] - nums[0]
        second = nums[-3] - nums[1]
        third = nums[-2] - nums[2]
        fourth = nums[-1] - nums[3]
        return min(first, second, third, fourth)
    
