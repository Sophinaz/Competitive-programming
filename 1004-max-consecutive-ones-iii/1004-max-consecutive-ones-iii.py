class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        def maximumones(nums,k):
            result = 0
            l = 0
            r = 0
            count = {0:0 , 1:0}
            while r < len(nums):
                count[nums[r]] += 1
                
                if r-l+1 - count[1] <= k:
                    result = max(result,r-l+1)
                    r+=1
                else:
                    count[nums[l]] -= 1
                    l+=1
            return result
        return maximumones(nums,k)


        