class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0
        l,r = 0,0
        count = 0
        track = 0
        while r <= len(nums):
            if r == len(nums):
                result = max(result,r-l-1)
                break
            if nums[r] == 1:
                r+=1
            else:
                if count == 0: 
                    count+=1
                    track = r
                else:
                    result = max(result, r-l-1)
                    l = track+1
                    track = r
                    count = 1
                r+=1
        return result