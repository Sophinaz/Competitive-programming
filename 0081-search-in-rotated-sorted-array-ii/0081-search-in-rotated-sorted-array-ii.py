class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        minn_index = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                minn_index = i

        right = len(nums) - 1
        left = minn_index
        
        if target >= nums[0] and minn_index != 0:
            right = minn_index
            left = 0

        while left <= right:
            mid = (left + right) // 2
            # print(left, right, mid)
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return True
        return False

