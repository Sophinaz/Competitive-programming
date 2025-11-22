class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid)
            if nums[mid] == target:
                return True

            if nums[left] == nums[mid]:
                left += 1
                continue

            if (nums[mid] > nums[-1] and target > nums[-1]) or (nums[mid] <= nums[-1] and target <= nums[-1]):
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] > target:
                    left = mid + 1
                else:
                    right = mid - 1
                
        
        if left < len(nums) and nums[left] == target:
            return True
        return False