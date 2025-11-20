class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in check and abs(check[nums[i]] - i) <= k:
                return True
            check[nums[i]] = i

        return False 