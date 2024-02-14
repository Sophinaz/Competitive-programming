class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        count = 0
        good = nums[-1]
        for i in range(len(nums)-1,0,-1):
            print(good)
            if nums[i-1] > count:
                good = nums[i-1]
                count = 0
                if i == 1: return True
            else: count += 1
        return False