class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = nums1
        if len(nums1) < len(nums2):
            count = Counter(nums1)
            nums = nums2
        else: count = Counter(nums2)
        result = []
        
        for i in nums:
            if i in count:
                result.append(i)
                count[i] -= 1
                if count[i] == 0: count.pop(i)
        return result

