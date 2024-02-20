class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        po = list(set(nums))
        po.sort()
        nums[:len(po)] = po
        return len(po)