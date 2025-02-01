class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def parity(num):
            if num % 2 == 0:
                return True
            return False

        for i in range(1, len(nums)):
            if parity(nums[i]) == parity(nums[i-1]):
                return False
            
        return True