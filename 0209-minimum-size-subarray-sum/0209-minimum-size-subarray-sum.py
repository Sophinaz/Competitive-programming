class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        result = float('inf')
        # nums = sorted(nums)
        temp = 0
        while r<len(nums):

            while temp + nums[r]>= target:
                result = min(result,r-l+1)
                temp -= nums[l]
                l+=1
            
            temp += nums[r]
            r+=1
        if result != float('inf'):
            return result
        else: return 0
