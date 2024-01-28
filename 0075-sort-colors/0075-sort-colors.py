class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tracker = {0:0,1:0,2:0}
        for i in nums:
            tracker[i] += 1
        idx = 0
        cummulative = 0
        for i in tracker:
            nums[idx:idx+tracker[i]] = [i]*tracker[i]
            cummulative += tracker[i]
            idx = cummulative
        return nums