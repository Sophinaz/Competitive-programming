class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = defaultdict(int)

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in track:
                return [track[difference], i]

            track[nums[i]] = i

        