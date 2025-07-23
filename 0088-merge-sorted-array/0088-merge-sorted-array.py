class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m-1
        right = n-1
        ptr = len(nums1) - 1
        if not n: return

        while left >= 0 and right >= 0:
            if nums1[left] >= nums2[right]:
                nums1[ptr] = nums1[left]
                left -= 1
                ptr -= 1
            else:
                nums1[ptr] = nums2[right]
                right -= 1
                ptr -= 1

        if right >= 0:
            for i in range(right, -1, -1):
                nums1[ptr] = nums2[i]
                ptr -= 1