class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        result = []
        def backtrack(path):
            if sum(path) == target:
                if sorted(path) not in result: result.append(sorted(path))
                return

            for i in range(len(nums)):
                if sum(path) < target:
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                # else: path.pop()
        backtrack([])
        return result