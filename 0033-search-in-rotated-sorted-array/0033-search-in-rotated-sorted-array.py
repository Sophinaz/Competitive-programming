class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_arr = True
        if target < nums[0]:
            left_arr = False
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if left_arr:
                if nums[mid] >= nums[0]:
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    right = mid - 1
            else:
                if nums[mid] < nums[0]:
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    left = mid + 1
        print(left)
        if left < 0 or left >= len(nums):
            return -1
        return left if nums[left] == target else -1