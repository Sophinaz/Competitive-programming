class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = 0
        want = float('inf')

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums) -1 
            while l<r:
                total = nums[l] + nums[r] + nums[i]
                diff = abs(total - target)
                if diff < want:
                    want = diff
                    ans = total

                if total > target:
                    r-=1
                else:
                    l+=1    
                    while nums[l] == nums[l-1] and l <r:
                        l+=1

        return ans

            