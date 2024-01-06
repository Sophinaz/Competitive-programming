class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)

        prep = 1
        postp = 1
        for i in range(len(nums)):
            pre[i] = prep
            prep*= nums[i]
        l = 0
        for i in range(len(nums)-1,-1,-1):
            post[i] = postp
            postp *= nums[i]
            l+=1
        answer = [1]*len(nums)
        for i in range(len(nums)):
            answer[i] = pre[i] * post[i]
        return answer
            
