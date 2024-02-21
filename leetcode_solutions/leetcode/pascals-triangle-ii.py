class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        level = rowIndex
        if level == 0: return [1]
        def getrow(level):
            if level == 1:
                return [1,1]
            ans = []
            arr = getrow(level-1)
            for i in range(1,len(arr)):
                ans.append(arr[i] + arr[i-1])
            return [1] + ans + [1]
        return getrow(level)