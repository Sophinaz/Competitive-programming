class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right = 0,0
        result = 0
        nums = s
        track = {}
        n = len(nums)
        while right < n:
            if nums[right]not in track: track[nums[right]] = 1
            else: track[nums[right]] += 1

            if right-left+1 - max(track.values()) <= k:
                result = max(result,right-left+1)
            else:
                track[nums[left]]-=1
                left+=1
            right +=1

        return result
        
