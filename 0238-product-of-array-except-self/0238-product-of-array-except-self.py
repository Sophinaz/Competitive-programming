class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        answer = [1] * len(nums)
        prep = 1
        postp = 1
        for i in range(len(nums)):
            answer[i] = prep
            prep*= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= postp
            postp *= nums[i]
            
        
    
        return answer
            
