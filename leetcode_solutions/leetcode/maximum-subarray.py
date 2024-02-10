class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        prefix = 0
        for i in nums:
            prefix += i
            result = max(prefix,result)
            if prefix < 0:
                prefix = 0
        return result 