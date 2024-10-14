class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        num = (k * 2) + 1
        result = [-1 for i in range(len(nums))]
        left = 0
        total = sum(nums[:num])
        if len(result) >= num:
            result[k] = total // num

        for right in range(num, len(nums)):
            total += nums[right]
            total -= nums[left]
            result[left + k + 1] = total // num
            left += 1

        return result