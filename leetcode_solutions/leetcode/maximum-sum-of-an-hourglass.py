class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        result = -1
        for i in range(len(grid)-2):
            for j in range(1,len(grid[i])-1):
                new = sum(grid[i][j-1:j+2]) + grid[i+1][j] + sum(grid[i+2][j-1:j+2])
                result = max(result,new)

        return result