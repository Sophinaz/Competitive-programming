class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for _, b in count.items():
            if b % 2:
                return False
        return True