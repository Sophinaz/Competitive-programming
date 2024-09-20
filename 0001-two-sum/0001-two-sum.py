class Solution(object):
    def twoSum(self, nums, target):

        def sumOfElements(nums,target):
            has = {}
            for i in range(len(nums)):
                dif = target - nums[i]
                if dif in has:
                    return [has[dif],i]
                has[nums[i]] = i
        return sumOfElements(nums,target)
                