class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums)/k
        n = len(nums)
        if target != int(target):
            return False
        nums.sort(reverse = True)
        
        @cache
        def backtrack(mask, subSum):
            if mask == (1<<n)-1:
                return True
            if subSum == target:
                return backtrack(mask, 0)
            possible = False
            for i in range(n):
                if not mask&(1<<i) and subSum +nums[i] <= target:
                    possible |= backtrack(mask|(1<<i), subSum + nums[i])
            return possible
        
        return backtrack(0,0)