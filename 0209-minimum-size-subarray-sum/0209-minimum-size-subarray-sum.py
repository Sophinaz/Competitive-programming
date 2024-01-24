class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        result = float('inf')
        # nums = sorted(nums)
        temp = 0
        while r<len(nums):
            temp += nums[r]

            while temp>= target:
                result = min(result,r-l+1)
                temp -= nums[l]
                l+=1
                
            r+=1
        if result != float('inf'):
            return result
        else: return 0
