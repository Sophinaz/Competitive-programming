class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = [[]]
        def backtrack(idx, path):
            if len(path) == n:
                return

            for i in range(idx,n):
                path.append(nums[i])
                if path not in result: result.append(path.copy())
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return result