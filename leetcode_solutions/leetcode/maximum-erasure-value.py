class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        total,left,right = 0,0,0
        track = defaultdict(int)
        result = 0
        
        while right < len(nums):
            track[nums[right]] += 1
            total += nums[right]

            while track[nums[right]] > 1:
                track[nums[left]] -= 1
                total -= nums[left]
                left += 1

            result = max(result,total)
            right += 1

        return result

