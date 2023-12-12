class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        def subarray(nums,k):
            result = 0
            l = 0
            
            product = 1
            for r in range(len(nums)):
                product *= nums[r] 
                
                   
                if product >= k:
                    while product >= k and l<=r:
                            product/=nums[l]
                            l+=1
                result += r-l+1
            return result
        return subarray(nums,k)