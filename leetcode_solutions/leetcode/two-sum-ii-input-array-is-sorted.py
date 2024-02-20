class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        left = 0
        right  = len(numbers) - 1

        while left < right:
            if nums[right] + nums[left] > target:
                right -= 1
            elif nums[right] + nums[left] < target:
                left += 1
            else: return [left+1,right+1]
