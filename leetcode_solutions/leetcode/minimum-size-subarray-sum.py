class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur,left,right = 0,0,0
        result = float('inf')
        n = len(nums)
        while right < n:
            # if right == n:
            #     result = min(result,right-left+1)
            cur += nums[right]
            while cur >= target:
                result = min(result,right-left+1)
                cur -= nums[left]
                left+=1
            right += 1
        if result == float('inf'): return 0
        else: return result