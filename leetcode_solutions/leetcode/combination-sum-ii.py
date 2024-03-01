class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []
        total = 0
        def backtrack(idx):
            nonlocal total
            if total == target:
                result.append(path[:])
                return

            if idx >= len(candidates): return

            if total < target:
                path.append(candidates[idx])
                total += candidates[idx]
                backtrack(idx+1)
                
                while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                    idx+=1
                x = path.pop()
                
                total -= x
                backtrack(idx+1)

        
        backtrack(0)
        
        return result