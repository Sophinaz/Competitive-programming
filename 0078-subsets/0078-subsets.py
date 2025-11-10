class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        maxx = 2 ** len(nums)
        result = []

        for number in range(maxx):
            temp_res = []
            idx = len(nums) - 1
            while number:
                if number & 1:
                    temp_res.append(nums[idx])
                idx -= 1
                number >>= 1
            result.append(temp_res)

        return result