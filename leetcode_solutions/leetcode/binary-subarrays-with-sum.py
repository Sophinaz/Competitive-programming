class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total,left = 0,0
        track = {0:1}
        result = 0
        for i in nums:
            total += i

            if total - goal in track:
                result += track[total-goal]
            track[total] =1 + track.get(total,0)

        return result 