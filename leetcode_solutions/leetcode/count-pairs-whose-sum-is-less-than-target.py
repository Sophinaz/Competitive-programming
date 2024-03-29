class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        nums = sorted(nums)
        result = 0
        while l < r:
            if nums[l] + nums[r] < target:
                result += r-l
                l+=1
            else:
                r-=1
                
        return result

        