class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1,10)]
        total = 0
        result = []
        def combine(i, path):
            nonlocal total
            if total == n and len(path) == k:
                if path not in result: result.append(path[:])
                return
            if len(path) == k or i > 8: return

            path.append(nums[i])
            total += nums[i]
            combine(i+1, path)
            
            x = path.pop()
            total -= x
            combine(i+1,path)
        
        combine(0,[])
        return result