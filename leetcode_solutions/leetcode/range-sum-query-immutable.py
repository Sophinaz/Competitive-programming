class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums 
        self.pre = [0] * len(nums)
        post = [0] * len(nums)
        self.pre[0] = nums[0]
        post[-1] = nums[-1]
        r = len(nums)-2
        for i in range(1,len(nums)):
            self.pre[i] = nums[i] + self.pre[i-1]       
            post[r] = nums[r] + post[r+1]
    def sumRange(self, left: int, right: int) -> int:
        if left-1<0:
            return self.pre[right]
        return self.pre[right]-self.pre[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)