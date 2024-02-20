class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left,right = 0,1

        while right < len(nums):
            while right < len(nums) and nums[left] == nums[right]:
                nums.pop(right)
            left += 1
            right += 1
        return len(nums)