class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                track = {}
                value = target - (nums[i] + nums[j])
                for k in range(j+1, len(nums)):
                    diff = value - nums[k]
                    if diff in track:
                        combination = sorted([nums[i], nums[j], nums[k], diff])
                        result.add(tuple(combination))
                    track[nums[k]] = i
           
        return list(result)
