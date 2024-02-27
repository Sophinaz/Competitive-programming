class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def Permute(path):
            if len(path) == n:
                result.append(path.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    Permute(path)
                    path.pop()
        Permute([])
        return result

            