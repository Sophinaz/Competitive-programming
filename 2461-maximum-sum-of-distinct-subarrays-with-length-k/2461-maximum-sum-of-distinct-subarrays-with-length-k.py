class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        track = defaultdict(int)
        result = 0
        left = 0
        total = 0

        for right in range(len(nums)):
            track[nums[right]] += 1
            total += nums[right]
            while left < right and track[nums[right]] > 1:
                track[nums[left]] -= 1
                if track[nums[left]] == 0:
                    track.pop(nums[left])
                total -= nums[left]
                left += 1

            if right - left + 1 == k:
                result = max(result, total)
                total -= nums[left]
                track[nums[left]] -= 1
                if track[nums[left]] == 0:
                    track.pop(nums[left])
                left += 1

        return result
