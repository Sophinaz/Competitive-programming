class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)-1

        while left <= right:
            idx = (left+right) // 2
            if nums[idx] < target:
                left = idx + 1
            elif nums[idx] > target:
                right = idx - 1
            else:
                return idx
        return -1