class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        middle_index = -1
        pre = [0] * len(nums)
        post = [0] * len(nums)
        for i in range(1,len(nums)):
            pre[i] = nums[i-1] + pre[i-1]
        for i in range(len(nums)-2,-1,-1):
            post[i] = nums[i+1] + post[i+1]
        combine = zip(pre,post)
        track = 0
        for i,j in combine:
            if i == j:
                return track
            track +=1
     
        return middle_index