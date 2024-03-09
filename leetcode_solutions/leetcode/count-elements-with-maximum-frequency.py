class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        result = 0
        num = max(count.values())

        for i in count:
            if count[i] == num: result += 1

        return result * num