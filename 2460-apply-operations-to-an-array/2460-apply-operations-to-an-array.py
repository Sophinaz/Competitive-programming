class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        left = 0
        def rig(l, nums):
            while  l < len(nums) and nums[l] != 0:
                l += 1
            return l
        left = rig(0, nums)

        for right in range(len(nums)):
            if left >= len(nums): break
            if nums[right] != 0 and right > left:
                nums[left], nums[right] = nums[right], nums[left]
                left = rig(left, nums)
            right -= 1

        return nums