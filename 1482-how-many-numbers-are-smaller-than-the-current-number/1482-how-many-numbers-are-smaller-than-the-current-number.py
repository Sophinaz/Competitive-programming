class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        count = {}

        s = sorted(nums)

        for i in range(n):
            answer[i] = s.index(nums[i])
        return answer


        

