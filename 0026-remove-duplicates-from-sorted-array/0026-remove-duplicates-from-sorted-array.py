class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        po = list(set(nums))
        nums[:len(po)] = po
        return len(po)