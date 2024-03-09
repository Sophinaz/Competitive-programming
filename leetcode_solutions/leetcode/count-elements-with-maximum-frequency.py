class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        result = 0
        maxx = 0

        for i in count:
            if count[i] == maxx: result += 1
            elif count[i] > maxx: 
                result = 1
                maxx = count[i] 

        return result * maxx