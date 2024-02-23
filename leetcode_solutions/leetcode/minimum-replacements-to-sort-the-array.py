class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > nums[i+1]:
                curr = math.ceil(nums[i] / nums[i+1])
                result += curr-1
                nums[i] = nums[i] // curr

        return result

                    
