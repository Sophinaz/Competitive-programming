class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        idx = 1
        result = 0
        while idx < n:
            result += nums[idx]
            idx +=2
        return result
