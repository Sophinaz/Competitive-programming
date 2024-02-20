class Solution(object):
    def largestNumber(self, nums):
        if (sum(nums)) == 0:
            return "0"
        def compare(x,y):
            return x+y > y+x
        nums = [str(i) for i in nums]
        nums.sort(reverse=True)
        j = 1
        for i in range(len(nums)-1):
            j = i+1
            while j < len(nums):
                if not compare(nums[i],nums[j]):
                    nums[i],nums[j] = nums[j],nums[i]
                j += 1
        return "".join(nums)
