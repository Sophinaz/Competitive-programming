class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        idx = arr.index(max(arr))
        if idx == 0 or idx == len(arr)-1: return False
        
        for i in range(1,idx + 1):
            if arr[i] <= arr[i-1]: return False
        for i in range(idx+1,n):
            if arr[i] >= arr[i-1]: return False
            
        return True
