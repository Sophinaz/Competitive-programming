class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if i % 2 and nums[i] != nums[i-1]:
                return nums[i-1]
            
            if i % 2 == 0 and i == len(nums) - 1:
                return nums[-1] 

        return nums[0]